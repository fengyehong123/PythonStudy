"""
    requests三方库并不支持异步 I/O
    如果希望使用异步 I/O 的方式来加速爬虫代码的执行
    我们可以安装和使用名为【aiohttp】的三方库。
"""
import re
import aiohttp
import asyncio

# 获取网页标题的正则表达式
TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.DOTALL)

async def fetch_page_title(url, session):
    try:
        # 向指定网页发起请求
        async with session.get(url, ssl=False, timeout=10) as resp:

            # 如果响应的状态码不是200
            if resp.status != 200:
                print(f"{url}: Failed with status {resp.status}")
                return
            
            # 获取网页的html代码
            html_code = await resp.text()

            # 通过正则表达式解析出网页的title
            matcher = TITLE_PATTERN.search(html_code)
            title = ""
            if matcher:
                title = matcher.group(1).strip()
            else:
                title = "没有找到网页标题"
            
            print(f"{url} → {title}")
                
    except Exception as e:
        print(f"{url}: Error {e}")

async def main():

    # 各个网页URL
    urls = [
        'https://www.python.org/',
        'https://www.jd.com/',
        'https://www.baidu.com/',
        'https://www.taobao.com/',
        'https://git-scm.com/',
        'https://www.sohu.com/',
        'https://gitee.com/',
        'https://www.amazon.com/',
        'https://www.usa.gov/',
        'https://www.nasa.gov/'
    ]

    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }

    # 创建http请求对象
    async with aiohttp.ClientSession(headers=headers) as session:

        # 发起异步请求，创建若干个Task
        tasks = [fetch_page_title(url, session) for url in urls]
        # 等待请求结束
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
