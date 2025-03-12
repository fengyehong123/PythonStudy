import os
import csv
import time
import random
import datetime
from concurrent.futures import ThreadPoolExecutor

"""参数配置"""
FILE_NAME = "person_data.csv"
OUTPUT_FILE = os.path.join(os.path.expanduser("~"), "Desktop", FILE_NAME)
# 总行数
ROWS = 5000000  
# 并行线程数
THREAD_COUNT = 4
# 每个线程的记录数
CHUNK_SIZE = (ROWS + THREAD_COUNT - 1) // THREAD_COUNT

# 确保文件不存在
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

"""生成部分CSV数据并写入临时文件"""
def generate_csv_chunk(start_row, end_row, temp_file):

    with open(temp_file, mode='w', newline='', encoding='utf-8') as f:

        random.seed()
        current_date = datetime.datetime.now()
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        
        for i in range(start_row, end_row + 1):
            row = [
                i,
                f"Name_{i}",
                random.randint(18, 60),
                f"user{i}@example.com",
                (current_date - datetime.timedelta(days=random.randint(0, 365))).strftime("%Y/%m/%d %H:%M:%S")
            ]
            writer.writerow(row)

"""合并所有临时 CSV 到最终文件"""
def merge_csv_files(output_file, temp_files):
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as out_f:

        for temp_file in sorted(temp_files):
            with open(temp_file, mode='r', encoding='utf-8') as temp_f:
                out_f.write(temp_f.read())
            os.remove(temp_file)
            
"""
    通过线程池的方式处理, 由于文件生成设计到CPU计算
    因此效率不如进程池
"""
def main():

    start_time = time.time()
    temp_files = []
    
    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:

        futures = []

        for i in range(THREAD_COUNT):

            start_row = i * CHUNK_SIZE + 1
            end_row = min((i + 1) * CHUNK_SIZE, ROWS)
            temp_file = f"{OUTPUT_FILE}.{i + 1}.part"
            temp_files.append(temp_file)

            futures.append(executor.submit(generate_csv_chunk, start_row, end_row, temp_file))
        
        for future in futures:
            # 等待所有任务完成
            future.result()
    
    print("临时CSV文件生成完毕，开始合并...")
    merge_csv_files(OUTPUT_FILE, temp_files)
    
    print(f"CSV 文件生成完毕，路径: {OUTPUT_FILE}")
    print(f"总耗时: {time.time() - start_time:.2f} 秒")

if __name__ == "__main__":
    main()
