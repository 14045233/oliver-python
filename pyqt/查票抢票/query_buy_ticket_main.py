import json
import sys
import re
from datetime import datetime, timedelta
import requests
import prettytable as pt
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from query_buy_ticket import Ui_Query_Buy_Ticket
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 忽视该警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Query_Buy_Ticket(QMainWindow, Ui_Query_Buy_Ticket):
    def __init__(self):
        super(Query_Buy_Ticket, self).__init__()
        self.ticket_option = "a"
        self.setupUi(self)
        self.show()
        self.pushButton_buy.clicked.connect(self.buy_ticket)
        self.pushButton_query.clicked.connect(self.query_ticket)

    def get_station_code(self):
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        response = requests.get(url, verify=False)
        stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
        station_dict = {station[0]: station[1] for station in stations}
        return station_dict

    def validate_input(self):
        ticket_option = self.lineEdit_option.text().replace(" ", "")
        from_station = self.lineEdit_from_station.text().replace(" ", "")
        to_station = self.lineEdit_to_station.text().replace(" ", "")
        train_date = self.lineEdit_train_date.text().replace(" ", "")
        if not ticket_option:
            QMessageBox.warning(self, "提示", "请输入有效的类型")
            return
        if from_station is None or to_station is None:
            QMessageBox.warning(self, "提示", "请输入有效的车站名")
            return
        try:
            date = datetime.strptime(train_date, "%Y-%m-%d")
        except ValueError:
            # 输入日期格式不正确
            QMessageBox.warning(self, "Warning", "Date format is incorrect.")
            return
        if date < datetime.now() or date > datetime.now() + timedelta(days=15):
            # 输入日期不在合法范围内
            QMessageBox.warning(self, "Warning", "Date should be between today and 15 days later.")
            return
        return from_station, to_station, train_date, ticket_option

    def buy_ticket(self):
        pass
    def query_ticket(self):
        from_station, to_station, train_date, ticket_option = self.validate_input()
        station_dict = self.get_station_code()
        # print(station_dict)
        url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={train_date}&leftTicketDTO.from_station={station_dict[from_station]}&leftTicketDTO.to_station={station_dict[to_station]}&purpose_codes=ADULT'
        headers = {
            "Cookie": "_uab_collina=167946560011909199771135; JSESSIONID=AE09B67A72C2407C1B9D79ED19F23DA8; RAIL_EXPIRATION=1679742222346; RAIL_DEVICEID=O5TwFeu4Kw_HGZF75ufekrzsLKPFJQv8vi0S8Fe5Dkit1oOkxAPbmg5itIlKjZmJVVxdwakU_EFpuNXVb_qNsVvmv23rZ5Dsjnj_vtwiTQXgaWVWlvR_bwP1dXIyByL96JbB5O29Hz28c1enfMyp1iSDP4IjbdRV; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_wfdc_flag=dc; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=4040622346.64545.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_toStation=%u8D63%u5DDE%2CBJP; _jc_save_fromDate=2023-05-15; _jc_save_toDate=2023-05-12; BIGipServerportal=3134456074.17183.0000",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
        }
        response = requests.get(url=url, headers=headers)
        tb = pt.PrettyTable()
        tb.field_names = [
            '序号',
            '车次',
            '出发地',
            '目的地',
            '出发时间',
            '到达时间',
            '耗时',
            '特等座',
            '一等',
            '二等',
            '软卧',
            '硬卧',
            '硬座',
            '无座',
        ]
        page = 1
        for index in response.json()['data']['result']:  # 把列表里面元素 一个一个提取出来, 用for循环遍历
            # index.split('|') # 字符串分割, 以|进行分割, 返回列表
            print(index)
            info = index.split('|')
            num = info[3]  # 车次
            from_station = next((k for k, v in station_dict.items() if v == info[6]), None)
            to_station = next((k for k, v in station_dict.items() if v == info[7]), None)
            start_time = info[8]  # 出发时间
            end_time = info[9]  # 到达时间
            use_time = info[10]  # 耗时
            topGrade = info[32]  # 特等座
            first_class = info[31]  # 一等
            second_class = info[30]  # 二等
            soft_sleeper = info[23]  # 软卧
            hard_sleeper = info[28]  # 硬卧
            hard_seat = info[29]  # 硬座
            no_seat = info[26]  # 无座
            tb.add_row([
                page,
                num,
                from_station,
                to_station,
                start_time,
                end_time,
                use_time,
                topGrade,
                first_class,
                second_class,
                soft_sleeper,
                hard_sleeper,
                hard_seat,
                no_seat,
            ])
            page += 1
        self.textBrowser.setText(str(tb))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    query_buy_ticket = Query_Buy_Ticket()
    sys.exit(app.exec())