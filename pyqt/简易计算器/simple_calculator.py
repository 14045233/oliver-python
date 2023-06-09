# Form implementation generated from reading ui file 'simple_calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(651, 449)
        Calculator.setStyleSheet("* {\n"
"    font-size: 16px;\n"
"     color: blue\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Calculator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_num1 = QtWidgets.QLabel(parent=Calculator)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_num1.setFont(font)
        self.label_num1.setObjectName("label_num1")
        self.horizontalLayout.addWidget(self.label_num1)
        self.lineEdit_num1 = QtWidgets.QLineEdit(parent=Calculator)
        self.lineEdit_num1.setObjectName("lineEdit_num1")
        self.horizontalLayout.addWidget(self.lineEdit_num1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_num2 = QtWidgets.QLabel(parent=Calculator)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_num2.setFont(font)
        self.label_num2.setObjectName("label_num2")
        self.horizontalLayout_2.addWidget(self.label_num2)
        self.lineEdit_num2 = QtWidgets.QLineEdit(parent=Calculator)
        self.lineEdit_num2.setText("")
        self.lineEdit_num2.setObjectName("lineEdit_num2")
        self.horizontalLayout_2.addWidget(self.lineEdit_num2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add = QtWidgets.QPushButton(parent=Calculator)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_sub = QtWidgets.QPushButton(parent=Calculator)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.horizontalLayout_3.addWidget(self.pushButton_sub)
        self.pushButton_mul = QtWidgets.QPushButton(parent=Calculator)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.horizontalLayout_3.addWidget(self.pushButton_mul)
        self.pushButton_divide = QtWidgets.QPushButton(parent=Calculator)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.horizontalLayout_3.addWidget(self.pushButton_divide)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_result = QtWidgets.QLabel(parent=Calculator)
        self.label_result.setMinimumSize(QtCore.QSize(433, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "简易计算器"))
        self.label_num1.setText(_translate("Calculator", "请输入第一个数字："))
        self.label_num2.setText(_translate("Calculator", "请输入第二个数字："))
        self.pushButton_add.setText(_translate("Calculator", "+"))
        self.pushButton_sub.setText(_translate("Calculator", "-"))
        self.pushButton_mul.setText(_translate("Calculator", "*"))
        self.pushButton_divide.setText(_translate("Calculator", "/"))
        self.label_result.setText(_translate("Calculator", "结果："))
