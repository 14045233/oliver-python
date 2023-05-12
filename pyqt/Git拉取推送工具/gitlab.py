# Form implementation generated from reading ui file 'gitlab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(795, 354)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 13, 783, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.repo_path_label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.repo_path_label.setFont(font)
        self.repo_path_label.setObjectName("repo_path_label")
        self.horizontalLayout.addWidget(self.repo_path_label)
        self.repo_path_edit = QtWidgets.QLineEdit(parent=self.widget)
        self.repo_path_edit.setObjectName("repo_path_edit")
        self.repo_path_edit.setText("git@github.com:14045233/Python.git")
        self.horizontalLayout.addWidget(self.repo_path_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.local_path_label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.local_path_label.setFont(font)
        self.local_path_label.setObjectName("local_path_label")
        self.horizontalLayout_2.addWidget(self.local_path_label)
        self.local_path_edit = QtWidgets.QLineEdit(parent=self.widget)
        self.local_path_edit.setObjectName("local_path_edit")
        self.local_path_edit.setText(r"D:\workbench\test")
        self.horizontalLayout_2.addWidget(self.local_path_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pull_btn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pull_btn.setFont(font)
        self.pull_btn.setObjectName("pull_btn")
        self.horizontalLayout_3.addWidget(self.pull_btn)
        self.push_btn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_btn.setFont(font)
        self.push_btn.setObjectName("push_btn")
        self.horizontalLayout_3.addWidget(self.push_btn)
        self.diff_btn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.diff_btn.setFont(font)
        self.diff_btn.setObjectName("diff_btn")
        self.horizontalLayout_3.addWidget(self.diff_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.repo_path_label.setText(_translate("Dialog", "Git仓库路径："))
        self.local_path_label.setText(_translate("Dialog", "本地仓库路径："))
        self.pull_btn.setText(_translate("Dialog", "从远程仓库拉取代码"))
        self.push_btn.setText(_translate("Dialog", "将本地仓库代码推送到远程仓库"))
        self.diff_btn.setText(_translate("Dialog", "比较本地仓库和远程仓库有什么变动"))
