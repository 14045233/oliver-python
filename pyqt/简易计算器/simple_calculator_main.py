import sys
from PyQt6.QtWidgets import (
    QMessageBox, QApplication, QDialog
)
from simple_calculator import  *

class MySimpleCalculator(QDialog, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton_add.clicked.connect(self.do_compute("add"))
        self.pushButton_sub.clicked.connect(self.do_compute("sub"))
        self.pushButton_mul.clicked.connect(self.do_compute("mul"))
        self.pushButton_divide.clicked.connect(self.do_compute("div"))

    def do_compute(self, method):
        def compute():
            num1 = self.lineEdit_num1.text()
            num2 = self.lineEdit_num2.text()
            try:
                num1 = float(num1)
            except:
                QMessageBox.warning(self, "信息提示", "输入的内容不是数字")
                return
            try:
                num2 = float(num2)
            except:
                QMessageBox.warning(self, "信息提示", "输入的内容不是数字")
                return
            symol = ""
            result = 0
            if method == "add":
                result = num1 + num2
                symol = "+"
            elif method == "sub":
                result = num1 - num2
                symol = "-"
            elif method == "mul":
                result = num1 * num2
                symol = "*"
            elif method == "div":
                if num2 == 0:
                    QMessageBox.warning(self, "信息提示", "除数不能为0")
                    return
                result = round(num1 / num2, 2)
                symol = "/"
            result_text = f"结果：{num1} {symol} {num2} = {result}"
            self.label_result.setText(result_text)
            QMessageBox.information(self, "信息提示", "计算成功")
        return compute


    def add(self):
        num1 = self.lineEdit_num1.text()
        try:
            num1 = float(num1)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        num2 = self.lineEdit_num2.text()
        try:
            num2 = float(num2)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        result = num1 + num2
        result_text = f"结果：{num1} + {num2} = {result}"
        self.label_result.setText(result_text)

    def sub(self):
        num1 = self.lineEdit_num1.text()
        try:
            num1 = float(num1)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        num2 = self.lineEdit_num2.text()
        try:
            num2 = float(num2)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        result = num1 - num2
        result_text = f"结果：{num1} - {num2} = {result}"
        self.label_result.setText(result_text)

    def mul(self):
        num1 = self.lineEdit_num1.text()
        try:
            num1 = float(num1)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        num2 = self.lineEdit_num2.text()
        try:
            num2 = float(num2)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        result = num1 * num2
        result_text = f"结果：{num1} * {num2} = {result}"
        self.label_result.setText(result_text)

    def rid(self):
        num1 = self.lineEdit_num1.text()
        try:
            num1 = float(num1)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        num2 = self.lineEdit_num2.text()
        try:
            num2 = float(num2)
        except:
            QMessageBox.warning(self, "信息提示", "输入内容有误")
        result = num1 / num2
        result_text = f"结果：{num1} / {num2} = {result}"
        self.label_result.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mysimplecalculator = MySimpleCalculator()
    sys.exit(app.exec())