import sys
from PyQt6.QtWidgets import QMessageBox, QApplication, QDialog
from BMI import Ui_BMI

class MyBMI(QDialog, Ui_BMI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(
            self.calculate
        )

    def calculate(self):
        weight = self.lineEdit_weight.text()
        try:
            weight = float(weight)
        except:
            QMessageBox.warning(self, "信息提示", "你输入的体重有误")
            return
        height = self.lineEdit_height.text()
        try:
            height = float(height)/100
        except:
            QMessageBox.warning(self, "信息提示", "你输入的身高有误")
            return
        BMI = round(weight / (height ** 2), 2)
        gold_weight = round(22 * (height ** 2), 2)
        if BMI <= 18.1:
            scope = "偏瘦"
        elif 18.5 < BMI < 23.9:
            scope = "正常"
        elif 24 < BMI <27.9:
            scope = "超重"
        elif BMI >= 28:
            scope = "肥胖"
        result_text = f"BMI：{BMI}，属于{scope} 您的理想体重为：{gold_weight}KG"
        self.label_result.setText(result_text)
        QMessageBox.information(self, "信息提示", "计算成功")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mybmi = MyBMI()
    sys.exit(app.exec())
