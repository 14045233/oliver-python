import requests
import json
import uuid
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class MyThread(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self) -> None:
        down_img(self.url)


def down_img(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers).text

    res_dic = json.loads(res)
    for item in res_dic["data"]:
        img_url = item.get("thumbURL", "")
        if img_url == "":
            continue

        img_data = requests.get(img_url, headers=headers).content

        with open(f"pics/{uuid.uuid4()}.jpg", "wb") as f:
            f.write(img_data)

if __name__ == "__main__":
    word = input("请输入你要爬取的关键字：")
    page_num = int(input("请输入你要爬取的页数："))

    urls = [f"https://image.baidu.com/search/acjson?"
            f"tn=resultjson_com&logid=81857455197772137621&"
            f"ipn=rj&ct=201326592&is=&fp=result&fr=&"
            f"word={word}&cg=star&queryWord={word}&lm=-1&"
            f"ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0"
            f"&hd=&latest=&copyright=&s=&se=&tab=&width=&"
            f"height=&face=0&istype=2&qc=&nc=1&expermode=&"
            f"nojc=&isAsync=&pn={(i + 1) * 30}&rn=30&gsm=1e"
            f"&1683544144021=" for i in range(page_num)]
    starttime = datetime.now()
    # for url in urls:
    #     down_img(url)

    with ThreadPoolExecutor(max_workers=5) as execute:
        for url in urls:
            execute.submit(MyThread(url).run)

    endtime = datetime.now()
    print(f"总共花了{(endtime - starttime).seconds}秒。")