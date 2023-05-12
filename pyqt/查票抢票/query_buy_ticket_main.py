import json
import sys
from datetime import datetime
import Station_Parse
import requests
import prettytable as pt
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from query_buy_ticket import Ui_Query_Buy_Ticket
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 忽视该警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 数据处理+显示
class Trains_Demo():
    # 初始化
    def __init__(self, textBrowser, raw_trains, option):
        self.headers = '车次： 车站： 时间： 历时： 商务/特等座： 一等座： 二等座： 高级软卧： 软卧： 动卧： 硬卧： 软座： 硬座： 无座：'.split()
        self.raw_trains = raw_trains
        self.option = option
        self.textBrowser = textBrowser
        self.textBrowser.clear()

    # 获取出发和到达站
    def get_from_to_station_name(self, data_list):
        self.from_station_name = data_list[6]
        self.to_station_name = data_list[7]
        self.from_to_station_name = Station_Parse.parse_station().disparse(
            self.from_station_name) + '-->' + Station_Parse.parse_station().disparse(self.to_station_name)
        return self.from_to_station_name

    # 获得出发和到达时间
    def get_start_arrive_time(self, data_list):
        self.start_arrive_time = data_list[8] + '-->' + data_list[9]
        return self.start_arrive_time

    # 解析trains数据(与headers依次对应)
    def parse_trains_data(self, data_list):
        return {
            'trips': data_list[3],
            'from_to_station_name': self.get_from_to_station_name(data_list),
            'start_arrive_time': self.get_start_arrive_time(data_list),
            'duration': data_list[10],
            'business_premier_seat': data_list[32] or '--',
            'first_class_seat': data_list[31] or '--',
            'second_class_seat': data_list[30] or '--',
            'senior_soft_sleep': data_list[21] or '--',
            'soft_sleep': data_list[23] or '--',
            'move_sleep': data_list[33] or '--',
            'hard_sleep': data_list[28] or '--',
            'soft_seat': data_list[24] or '--',
            'hard_seat': data_list[29] or '--',
            'no_seat': data_list[26] or '--',
        }

    # 判断是否需要显示
    def need_show(self, data_list):
        self.trips = data_list[3]
        initial = self.trips[0].lower()
        if 'a' in self.option:
            return self.trips
        else:
            return (initial in self.option)

    # 数据显示
    def show_train_data(self):
        self.t_num = 0
        for self.train in self.raw_trains:
            self.data_list = self.train.split('|')
            if self.need_show(self.data_list):
                self.values_row = []
                self.parsed_train_data = self.parse_trains_data(self.data_list)
                self.values_row.append(self.headers[0] + self.parsed_train_data['trips'])
                self.values_row.append(self.headers[1] + self.parsed_train_data['from_to_station_name'])
                self.values_row.append(self.headers[2] + self.parsed_train_data['start_arrive_time'])
                self.values_row.append(self.headers[3] + self.parsed_train_data['duration'])
                self.values_row.append(self.headers[4] + self.parsed_train_data['business_premier_seat'])
                self.values_row.append(self.headers[5] + self.parsed_train_data['first_class_seat'])
                self.values_row.append(self.headers[6] + self.parsed_train_data['second_class_seat'])
                self.values_row.append(self.headers[7] + self.parsed_train_data['senior_soft_sleep'])
                self.values_row.append(self.headers[8] + self.parsed_train_data['soft_sleep'])
                self.values_row.append(self.headers[9] + self.parsed_train_data['move_sleep'])
                self.values_row.append(self.headers[10] + self.parsed_train_data['hard_sleep'])
                self.values_row.append(self.headers[11] + self.parsed_train_data['soft_seat'])
                self.values_row.append(self.headers[12] + self.parsed_train_data['hard_seat'])
                self.values_row.append(self.headers[13] + self.parsed_train_data['no_seat'])
                self.t_num += 1
                self.textBrowser.append('第%d班：' % self.t_num + '*' * 80)
                self.textBrowser.append('\n')
                self.textBrowser.append(" ".join(self.values_row))
                self.textBrowser.append('\n')


class Query_Buy_Ticket(QMainWindow, Ui_Query_Buy_Ticket):
    def __init__(self):
        super(Query_Buy_Ticket, self).__init__()
        self.ticket_option = "a"
        self.setupUi(self)
        self.show()
        self.pushButton_buy.clicked.connect(self.buy_ticket)
        self.pushButton_query.clicked.connect(self.query_ticket)


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
        if train_date:
            if datetime.strptime(train_date, '%Y-%m-%d') < datetime.now():
                QMessageBox.warning(self, "提示", "请输入有效日期")
                return
        else:
            QMessageBox.warning(self, "提示", "请输入有效日期")
            return
        return from_station, to_station, train_date, ticket_option

    def buy_ticket(self):
        pass

    def query_ticket(self):
        from_station, to_station, train_date, ticket_option = self.validate_input()
        with open("city.json", encoding="utf-8") as f:
            station_data = json.loads(f.read())
        url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={train_date}&leftTicketDTO.from_station={station_data[from_station]}&leftTicketDTO.to_station={station_data[to_station]}&purpose_codes=ADULT'
        headers = {
            "Cookie": "_uab_collina=167946560011909199771135; JSESSIONID=AE09B67A72C2407C1B9D79ED19F23DA8; RAIL_EXPIRATION=1679742222346; RAIL_DEVICEID=O5TwFeu4Kw_HGZF75ufekrzsLKPFJQv8vi0S8Fe5Dkit1oOkxAPbmg5itIlKjZmJVVxdwakU_EFpuNXVb_qNsVvmv23rZ5Dsjnj_vtwiTQXgaWVWlvR_bwP1dXIyByL96JbB5O29Hz28c1enfMyp1iSDP4IjbdRV; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_wfdc_flag=dc; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=4040622346.64545.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_toStation=%u8D63%u5DDE%2CBJP; _jc_save_fromDate=2023-05-15; _jc_save_toDate=2023-05-12; BIGipServerportal=3134456074.17183.0000",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
        }
        response = requests.get(url=url, headers=headers)

        '''
        self.trains = response.json()['data']['result']
        Trains_Demo(self.textBrowser, self.trains, self.ticket_option).show_train_data()
        '''

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
            from_station = next((k for k, v in station_data.items() if v == info[6]), None)
            to_station = next((k for k, v in station_data.items() if v == info[7]), None)
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