# Form implementation generated from reading ui file 'query_buy_ticket.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Query_Buy_Ticket(object):
    def setupUi(self, Query_Buy_Ticket):
        Query_Buy_Ticket.setObjectName("Query_Buy_Ticket")
        Query_Buy_Ticket.resize(705, 469)
        self.centralwidget = QtWidgets.QWidget(parent=Query_Buy_Ticket)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_passenger = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_passenger.setObjectName("label_passenger")
        self.horizontalLayout.addWidget(self.label_passenger)
        self.label_from_station = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_from_station.setObjectName("label_from_station")
        self.horizontalLayout.addWidget(self.label_from_station)
        self.label_to_station = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_to_station.setObjectName("label_to_station")
        self.horizontalLayout.addWidget(self.label_to_station)
        self.label_train_date = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_train_date.setObjectName("label_train_date")
        self.horizontalLayout.addWidget(self.label_train_date)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_passenger = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_passenger.setObjectName("lineEdit_passenger")
        self.horizontalLayout_2.addWidget(self.lineEdit_passenger)
        self.lineEdit_from_station = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_from_station.setObjectName("lineEdit_from_station")
        self.horizontalLayout_2.addWidget(self.lineEdit_from_station)
        self.lineEdit_to_station = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_to_station.setObjectName("lineEdit_to_station")
        self.horizontalLayout_2.addWidget(self.lineEdit_to_station)
        self.lineEdit_train_date = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_train_date.setObjectName("lineEdit_train_date")
        self.horizontalLayout_2.addWidget(self.lineEdit_train_date)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_option = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_option.setObjectName("label_option")
        self.verticalLayout_2.addWidget(self.label_option)
        self.label_user = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_user.setObjectName("label_user")
        self.verticalLayout_2.addWidget(self.label_user)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_option = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_option.setObjectName("lineEdit_option")
        self.verticalLayout_3.addWidget(self.lineEdit_option)
        self.lineEdit_user = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.verticalLayout_3.addWidget(self.lineEdit_user)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_order = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_order.setObjectName("label_order")
        self.verticalLayout_4.addWidget(self.label_order)
        self.label_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_password.setObjectName("label_password")
        self.verticalLayout_4.addWidget(self.label_password)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_order = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_order.setObjectName("lineEdit_order")
        self.verticalLayout_5.addWidget(self.lineEdit_order)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_5.addWidget(self.lineEdit_password)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_query = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton_query.setObjectName("pushButton_query")
        self.pushButton_buy = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.horizontalLayout_5.addWidget(self.splitter)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 1)
        Query_Buy_Ticket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Query_Buy_Ticket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menubar.setObjectName("menubar")
        Query_Buy_Ticket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Query_Buy_Ticket)
        self.statusbar.setObjectName("statusbar")
        Query_Buy_Ticket.setStatusBar(self.statusbar)

        self.retranslateUi(Query_Buy_Ticket)
        QtCore.QMetaObject.connectSlotsByName(Query_Buy_Ticket)

    def retranslateUi(self, Query_Buy_Ticket):
        _translate = QtCore.QCoreApplication.translate
        Query_Buy_Ticket.setWindowTitle(_translate("Query_Buy_Ticket", "查票购票工具"))
        self.label_passenger.setText(_translate("Query_Buy_Ticket", "乘客名："))
        self.label_from_station.setText(_translate("Query_Buy_Ticket", "出发地："))
        self.label_to_station.setText(_translate("Query_Buy_Ticket", "目的地："))
        self.label_train_date.setText(_translate("Query_Buy_Ticket", "日期(2023-05-15)："))
        self.lineEdit_from_station.setText(_translate("Query_Buy_Ticket", "上海"))
        self.lineEdit_to_station.setText(_translate("Query_Buy_Ticket", "赣州"))
        self.lineEdit_train_date.setText(_translate("Query_Buy_Ticket", "2023-05-15"))
        self.label_option.setText(_translate("Query_Buy_Ticket", "类型(查询用)："))
        self.label_user.setText(_translate("Query_Buy_Ticket", "用户名(抢票用)："))
        self.lineEdit_option.setText(_translate("Query_Buy_Ticket", "火车"))
        self.label_order.setText(_translate("Query_Buy_Ticket", "车次(抢票用)："))
        self.label_password.setText(_translate("Query_Buy_Ticket", "密码(抢票用)："))
        self.pushButton_query.setText(_translate("Query_Buy_Ticket", "查询"))
        self.pushButton_buy.setText(_translate("Query_Buy_Ticket", "抢票"))
