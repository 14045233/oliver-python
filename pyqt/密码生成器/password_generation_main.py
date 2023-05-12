import sys
import string
import random
from PyQt6.QtWidgets import (
    QMessageBox, QDialog, QApplication
)
from password_generation import Ui_Dialog


class MyPasswordGeneration(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(
            self.new_password
        )

    def new_password(self):
        site = self.lineEdit_site.text()
        if not site:
            QMessageBox.warning(self, "信息提示", "请输入site")
            return
        words = []
        if self.checkBox_upper.isChecked():
            words.append(string.ascii_uppercase)

        if self.checkBox_lower.isChecked():
            words.append(string.ascii_lowercase)

        if self.checkBox_number.isChecked():
            words.append(string.digits)

        if self.checkBox_puc.isChecked():
            words.append(string.punctuation)

        if not words:
            words = (
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits
                + string.punctuation
            )
        else:
            words = "".join(words)
        words = random.sample(list(words), 10)
        password = "".join(words)
        self.lineEdit_result.setText(password)

        QMessageBox.information(self, "信息提示", "密码生成成功")
        with open("密码本.txt", "a", encoding="utf-8") as f:
            f.write(f"{site}\t{password}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mypasswordgeneretion = MyPasswordGeneration()

    sys.exit(app.exec())