# Form implementation generated from reading ui file 'password_generation.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 173)
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 11, 562, 156))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_site = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_site.setObjectName("lineEdit_site")
        self.horizontalLayout_2.addWidget(self.lineEdit_site)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_upper = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.checkBox_upper.setFont(font)
        self.checkBox_upper.setObjectName("checkBox_upper")
        self.horizontalLayout.addWidget(self.checkBox_upper)
        self.checkBox_lower = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.checkBox_lower.setFont(font)
        self.checkBox_lower.setObjectName("checkBox_lower")
        self.horizontalLayout.addWidget(self.checkBox_lower)
        self.checkBox_number = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.checkBox_number.setFont(font)
        self.checkBox_number.setObjectName("checkBox_number")
        self.horizontalLayout.addWidget(self.checkBox_number)
        self.checkBox_puc = QtWidgets.QCheckBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.checkBox_puc.setFont(font)
        self.checkBox_puc.setObjectName("checkBox_puc")
        self.horizontalLayout.addWidget(self.checkBox_puc)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lineEdit_result = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.verticalLayout.addWidget(self.lineEdit_result)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请输入网站："))
        self.checkBox_upper.setText(_translate("Dialog", "大写字母"))
        self.checkBox_lower.setText(_translate("Dialog", "小写字母"))
        self.checkBox_number.setText(_translate("Dialog", "数字"))
        self.checkBox_puc.setText(_translate("Dialog", "标点符号"))
        self.pushButton.setText(_translate("Dialog", "生成新密码"))
