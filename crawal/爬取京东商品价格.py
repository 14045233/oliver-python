import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    word = input("请输入爬取关键字:")
    page_num = int(input("输入爬取的页数:"))
    driver = webdriver.Edge()
    driver.get("https://www.jd.com/")

    input_box = driver.find_element(By.ID, "key")
    input_box.send_keys(word)
    input_box.send_keys(Keys.ENTER)
    prices, titles, commits, shops = [], [], [], []
    for i in range(page_num):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        items = driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')
        for item in items:
            price = item.find_element(By.CLASS_NAME, "p-price").text
            title = item.find_element(By.CLASS_NAME, "p-name").text
            commit = item.find_element(By.CLASS_NAME, "p-commit").text
            shop = item.find_element(By.CLASS_NAME, "p-shop").text

            print(price, title, commit, shop)
            prices.append(price)
            titles.append(title)
            commits.append(commit)
            shops.append(shop)
        driver.find_element(By.CLASS_NAME, "pn-next").click()
        time.sleep(3)

    data = {
        'titles': titles,
        'prices': prices,
        'commits': commits,
        'shops': shops
    }
    df = pd.DataFrame(data=data)
    df.to_excel("book.xlsx", index=False)
    # print(data)
    time.sleep(10000)
