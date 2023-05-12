import re
import json
import requests

# 获取所有火车站和对应的代码
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
response = requests.get(url, verify=False)
stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
station_dict = {station[0]: station[1] for station in stations}

# 将字典转换为 JSON 格式并写入文件
with open('city.json', 'w', encoding='utf-8') as f:
    json.dump(station_dict, f, ensure_ascii=False)