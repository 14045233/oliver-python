# Form implementation generated from reading ui file 'json_formate_tool.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_JsonFormate(object):
    def setupUi(self, JsonFormate):
        JsonFormate.setObjectName("JsonFormate")
        JsonFormate.resize(571, 344)
        self.verticalLayout = QtWidgets.QVBoxLayout(JsonFormate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=JsonFormate)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=JsonFormate)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_format = QtWidgets.QPushButton(parent=JsonFormate)
        self.pushButton_format.setObjectName("pushButton_format")
        self.horizontalLayout.addWidget(self.pushButton_format)
        self.pushButton_unformat = QtWidgets.QPushButton(parent=JsonFormate)
        self.pushButton_unformat.setObjectName("pushButton_unformat")
        self.horizontalLayout.addWidget(self.pushButton_unformat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_copy = QtWidgets.QPushButton(parent=JsonFormate)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.verticalLayout.addWidget(self.pushButton_copy)

        self.retranslateUi(JsonFormate)
        QtCore.QMetaObject.connectSlotsByName(JsonFormate)

    def retranslateUi(self, JsonFormate):
        _translate = QtCore.QCoreApplication.translate
        JsonFormate.setWindowTitle(_translate("JsonFormate", "Json格式化工具"))
        self.label.setText(_translate("JsonFormate", "请输入粘贴的Json文本："))
        self.pushButton_format.setText(_translate("JsonFormate", "格式化Json"))
        self.pushButton_unformat.setText(_translate("JsonFormate", "反格式化Json"))
        self.pushButton_copy.setText(_translate("JsonFormate", "复制内容"))
