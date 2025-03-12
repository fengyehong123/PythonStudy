import os
import csv
import time
import random
import shutil
import datetime

from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

"""参数配置"""
# 总行数
ROWS = 5_000_000
# 文件名
FILE_NAME = "person_data.csv"

# 桌面文件对象
file_path = Path.home() / "Desktop" / FILE_NAME
# 桌面文件绝对路径
OUTPUT_FILE = file_path.resolve()

# 并行进程数（通常设为 CPU 核心数）, 此处暂时设置为4线程
PROCESS_COUNT = 4 or os.cpu_count()
# PROCESS_COUNT = os.cpu_count()

# 每个进程处理的记录数
CHUNK_SIZE = (ROWS + PROCESS_COUNT - 1) // PROCESS_COUNT

# 确保文件不存在
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

"""生成部分CSV数据并写入临时文件"""
def generate_csv_chunk(start_row, end_row, temp_file):

    random.seed()
    # 日期的格式
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
    # 获取当前日期
    current_date = datetime.datetime.now()

    with open(temp_file, mode='w', newline='', encoding='utf-8') as f:
        """
            quoting=csv.QUOTE_ALL
                给csv文件的每个字段都加上双引号
        """
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in range(start_row, end_row + 1):
            row = [
                i,
                f"Name_{i}",
                random.randint(18, 60),
                f"你好{i}@example.com",
                # 随机日期
                (current_date - datetime.timedelta(days=random.randint(0, 365))).strftime(DATE_FORMAT)
            ]
            # 将一行数据写入csv文件
            writer.writerow(row)
    
    return f"{Path(temp_file).name}的临时文件写入创建成功..."

"""合并所有临时 CSV 到最终文件"""
def merge_csv_files(output_file, temp_files):

    with open(output_file, mode='wb') as out_f:
        # 将临时文件排序后循环打开，然后依次写入
        for temp_file in sorted(temp_files):
            with open(temp_file, mode='rb') as temp_f:
                # shutil.copyfileobj() 直接拷贝二进制数据，比 read() + write() 方式更快，减少 I/O 负担。
                shutil.copyfileobj(temp_f, out_f)

def main():

    start_time = time.time()
    temp_files = []
    
    # 设置进程池，使用 Python的 【concurrent.futures】 模块提供的多进程执行器，用于执行 CPU 密集型任务，突破 GIL（全局解释器锁）的限制。
    with ProcessPoolExecutor(max_workers=PROCESS_COUNT) as executor:

        # 用于存储所有 提交到进程池的任务
        futures = []

        for i in range(PROCESS_COUNT):

            start_row = i * CHUNK_SIZE + 1
            end_row = min((i + 1) * CHUNK_SIZE, ROWS)

            # 获取临时文件的路径，然后添加到列表中
            temp_file = f"{OUTPUT_FILE}.{i + 1}.part"
            temp_files.append(temp_file)

            # 非阻塞地 将任务提交给进程池, 进程池中的每个进程都会执行 generate_csv_chunk(start_row, end_row, temp_file)
            task = executor.submit(generate_csv_chunk, start_row, end_row, temp_file)
            futures.append(task)
        
        # future.result() 是阻塞的，它会等待每个任务执行完毕，然后返回结果
        for future in futures:
            # 等待所有任务完成，还可以获取并发任务的返回值
            task_reult = future.result()
            print(task_reult)
    
    print('\033[91m临时 CSV 文件生成完毕，开始合并...\033[0m')
    merge_csv_files(OUTPUT_FILE, temp_files)

    # 批量删除临时文件
    for temp_file in temp_files:
        os.remove(temp_file)
    
    print(f'\033[91mCSV 文件合并完毕，路径: {OUTPUT_FILE}\033[0m')
    print(f'\033[91m总耗时: {time.time() - start_time:.2f} 秒\033[0m')

if __name__ == "__main__":
    main()
