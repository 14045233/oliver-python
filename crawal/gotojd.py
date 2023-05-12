import requests
from bs4 import BeautifulSoup

def jd_spider(keyword, pages):
    base_url = 'https://search.jd.com/Search?keyword={}&page={}'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}

    for page in range(1, pages+1):
        url = base_url.format(keyword, page)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        goods_list = soup.find_all('div', class_='gl-i-wrap')

        for goods in goods_list:
            # 获取商品名称
            name = goods.find('div', class_='p-name').find('em').text
            # 获取商品价格
            price = goods.find('div', class_='p-price').find('i').text
            # 获取商品评论数
            comment = goods.find('div', class_='p-commit').find('a').text
            # 获取店铺名称
            shop = goods.find('div', class_='p-shop').find('a').text

            # 输出数据
            print('商品名称：', name.strip())
            print('商品价格：', price.strip())
            print('商品评论：', comment.strip())
            print('店铺名称：', shop.strip())
            print('-' * 50)

if __name__ == '__main__':
    keyword = input('请输入要搜索的关键字：')
    pages = int(input('请输入要爬取的页数：'))
    jd_spider(keyword, pages)