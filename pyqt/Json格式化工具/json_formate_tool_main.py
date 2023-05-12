import json
import sys
from PyQt6.QtWidgets import (
    QMessageBox, QApplication, QDialog
)

from json_formate_tool import Ui_JsonFormate

class MyJsonFormate(Ui_JsonFormate, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton_format.clicked.connect(
            self.do_format_json("format")
        )
        self.pushButton_unformat.clicked.connect(
            self.do_format_json("unformat")
        )
        self.pushButton_copy.clicked.connect(
            self.do_copy_json
        )

    def do_format_json(self, type):
        def inner_format():
            json_cont = self.plainTextEdit.toPlainText()
            if not json_cont:
                QMessageBox.warning(self, "信息提示", "请输入内容")
                return
            try:
                if type == "format":
                    new_cont = json.dumps(
                        json.loads(json_cont),
                        indent=4,
                        ensure_ascii=False
                    )
                else:
                    new_cont = json.dumps(
                        json.loads(json_cont),
                        ensure_ascii=False
                    )
                self.plainTextEdit.setPlainText(new_cont)
                QMessageBox.information(self, "信息提示", "操作成功")
            except Exception as e:
                QMessageBox.warning(self, "信息提示", f"Json文本有问题，报错信息{str(e)}")
        return inner_format


    def do_copy_json(self):
        board = QApplication.clipboard()
        board.setText(self.plainTextEdit.toPlainText())
        QMessageBox.information(self, "信息提示", "复制成功")

# data = {
#     "小明": {
#         "学号": 123,
#         "性别": "男",
#         "爱好": "刷抖音,学Python"
#     },
#     "小张": {
#         "学号": 124,
#         "性别": "男",
#         "爱好": "刷抖音,学跳舞"
#     },
#     "小花": {
#         "学号": 125,
#         "性别": "女",
#         "爱好": "学Python,吃大肉"
#     }
# }

# undata = {"小明": {"学号": 123, "性别": "男", "爱好": "刷抖音,学Python"}, "小张": {"学号": 124, "性别": "男", "爱好": "刷抖音,学跳舞"}, "小花": {"学号": 125, "性别": "女", "爱好": "学Python,吃大肉"}}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myjsonformate = MyJsonFormate()
    sys.exit(app.exec())
