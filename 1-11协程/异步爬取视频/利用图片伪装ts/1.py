import aiohttp, aiofiles, os, asyncio, re
from aiohttp import TCPConnector
from pathlib import Path

async def get_url(url, YuMing, key):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as res:
            str_content = await res.text(encoding="utf-8")
            lines = str_content.split("\n")
            ts_line = next((line for line in lines if not line.startswith("#")), None)
            if ts_line:
                get_ts_url = f"https://{YuMing}/{key}/{ts_line}"
                print(get_ts_url)
                await get_ts(get_ts_url, headers)

async def get_ts(get_ts_url, headers):
    TsRegxes = re.compile(r'#EXTINF:.*?\n(.*?)\n')
    async with aiohttp.ClientSession() as session:
        async with session.get(get_ts_url, headers=headers) as res:
            ts_str = await res.text(encoding="utf-8")
            async with aiofiles.open("1-11协程/异步爬取视频/ts.txt", "w", encoding="utf-8") as fp:
                await fp.write(ts_str)
            print(res.status)
            ts_list = TsRegxes.findall(ts_str)

            ts_download_list = []
            for i, ts_file in enumerate(ts_list):
                ts_download_list.append((ts_file.strip(), f"{i}.ts"))

    await ts_download_all(ts_download_list)

async def download_one(url, name, sem):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    while True:
        async with sem:
            try:
                async with aiohttp.ClientSession(connector=TCPConnector(ssl=False), headers=headers) as session:
                    async with session.get(url, timeout=60) as res:
                        data = await res.read()
                        # 检查文件头是否为PNG或JPEG，并移除
                        if data.startswith(b'\x89PNG\r\n\x1a\n'):
                            data = data[8:]
                            print(f"Removed PNG header from {url}")
                        elif data.startswith(b'\xff\xd8\xff'):
                            data = data[3:]
                            print(f"Removed JPEG header from {url}")
                        async with aiofiles.open(f"1-11协程/异步爬取视频/ts/{name}", "wb") as fp:
                            await fp.write(data)
                        print(url, "======下载成功")
                        break
            except Exception as e:
                print(url, f"======下载失败，正在重新下载: {e}")

async def ts_download_all(ts_download_list):
    sem = asyncio.Semaphore(200)
    task_list = []
    for url, name in ts_download_list:
        cor = download_one(url, name, sem)
        task = asyncio.create_task(cor)
        task_list.append(task)
    await asyncio.wait(task_list)

def do_m3u8_url():
    with open("1-11协程/异步爬取视频/ts.txt", "r") as fp:
        data = fp.readlines()
    with open("1-11协程/异步爬取视频/ts/ts.m3u8", "w") as f:
        i = 0
        for line in data:
            if line.startswith("#"):
                f.write(line)
            else:
                f.write(f"{i}.ts\n")
                i += 1

def merge(filename):
    cmd = f'ffmpeg -allowed_extensions ALL -i 1-11协程/异步爬取视频/ts/ts.m3u8 -c copy 1-11协程/异步爬取视频/视频/{filename}.mp4'
    os.system(cmd)

def resolve_ts(src_path, dst_path):
    '''
    如果m3u8返回的ts文件地址为
    https://p1.eckwai.com/ufile/adsocial/7ead0935-dd4f-4d2f-b17d-dd9902f8cc77.png
    则需要下面处理后 才能进行合并
    原因在于 使用Hexeditor打开后，发现文件头被描述为了PNG或JPEG
    在这种情况下，只需要将其中PNG或JPEG文件头部分全部使用FF填充，即可处理该问题
    :return:
    '''
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)  # 创建目标路径目录，如果不存在的话
    elif not os.path.isdir(dst_path):
        raise ValueError(f"The destination path {dst_path} is not a directory.")
    
    file_list = os.listdir(src_path)
    valid_files = []

    for i in file_list:
        base_name, ext = os.path.splitext(i)
        if ext == '.ts':
            try:
                # 尝试将文件名（不包括扩展名）转换为整数
                parts = base_name.split('_')
                number_part = parts[0] if '_' in base_name else base_name
                int(number_part)
                valid_files.append(i)
            except ValueError:
                print(f"Skipping non-integer named file: {i}")
                continue
    
    file_list = sorted(valid_files, key=lambda x: int(x.split('.')[0].split('_')[0]) if '_' in x else int(x.split('.')[0]))

    for i in file_list:
        origin_ts = os.path.join(src_path, i)
        resolved_ts = os.path.join(dst_path, i)
        try:
            with open(origin_ts, "rb") as infile, open(resolved_ts, "wb") as outfile:
                data = infile.read()
                # 检查文件头是否为PNG或JPEG，并移除
                if data.startswith(b'\x89PNG\r\n\x1a\n'):
                    data = data[8:]
                elif data.startswith(b'\xff\xd8\xff'):
                    data = data[3:]
                outfile.write(data)
                outfile.seek(0x00)
                outfile.write(b'\xff\xff\xff\xff')
        except Exception as e:
            print(f"Failed to process {origin_ts}: {e}")
            continue
        print(f'Resolved {origin_ts} successfully')
def delete_ts():
    ts_m3u8_path = "1-11协程/异步爬取视频/ts/ts.m3u8"
    if os.path.exists(ts_m3u8_path):
        os.unlink(ts_m3u8_path)

    ts_dir = Path("1-11协程/异步爬取视频/ts")
    if ts_dir.exists() and ts_dir.is_dir():
        for i in ts_dir.glob('*.ts'):
            os.unlink(i)

async def main():
    url = input("输入m3u8地址: ")
    name = input("名字：")
    regexes = re.compile(r'^https://(.*?)/(.*)?/index.m3u8', re.VERBOSE)
    ls = regexes.findall(url)
    YuMing, key = ls[0]

    print("开始爬取")
    await get_url(url, YuMing, key)
    do_m3u8_url()

    resolve_ts("1-11协程/异步爬取视频/ts", "1-11协程/异步爬取视频/ts")
    merge(filename=name)
    delete_ts()

if __name__ == "__main__":
    asyncio.run(main())
