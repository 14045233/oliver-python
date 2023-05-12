import os
import re
import sys
import stat
import shutil
from git import Repo
from PyQt6.QtWidgets import (
    QMessageBox, QApplication, QDialog
)
from gitlab import Ui_Dialog

def is_git_url(url):
    # 匹配HTTPS协议的Git地址格式
    pattern = r'^https://.*\.git$'
    if re.match(pattern, url):
        return True

    # 匹配SSH协议的Git地址格式
    pattern = r'^git@.*:.*\.git$'
    if re.match(pattern, url):
        return True

    # 无法匹配任何格式
    return False

def readonly_handler(func, path, execinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

class MyGitlab(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pull_btn.clicked.connect(
            self.pull_from_remote
        )
        self.push_btn.clicked.connect(
            self.push_to_remote
        )
        self.diff_btn.clicked.connect(
            self.compare_local_remote
        )

    def pull_from_remote(self):
        repo_path = self.repo_path_edit.text()
        if os.path.exists(self.local_path_edit.text()):
            shutil.rmtree(self.local_path_edit.text(), onerror=readonly_handler)
        if not repo_path:
            QMessageBox.warning(self, "错误", "请填写Git仓库路径")
            return
        if not is_git_url(repo_path):
            QMessageBox.warning(self, "错误", "请填写正确的Git仓库路径")
            return
        local_path = self.local_path_edit.text()
        if not local_path:
            QMessageBox.warning(self, "错误", "请填写local仓库路径")
            return
        try:
            Repo.clone_from(repo_path, to_path=local_path)
            QMessageBox.information(self, "信息", "从远程仓库拉取代码成功")
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    def push_to_remote(self):
        repo_path = self.repo_path_edit.text()
        if not repo_path:
            QMessageBox.warning(self, "错误", "请填写Git仓库路径")
            return
        if not is_git_url(repo_path):
            QMessageBox.warning(self, "错误", "请填写正确的Git仓库路径")
            return
        local_path = self.local_path_edit.text()
        if not local_path:
            QMessageBox.warning(self, "错误", "请填写local仓库路径")
            return
        try:
            repo = Repo(self.local_path_edit.text())
            g = repo.git
            g.add("--all")
            g.commit('-m auto update')
            g.push()
            QMessageBox.information(self, "信息", "推送成功")
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

    def compare_local_remote(self):
        repo_path = self.repo_path_edit.text()
        if not repo_path:
            QMessageBox.warning(self, "错误", "请填写Git仓库路径")
            return
        if not is_git_url(repo_path):
            QMessageBox.warning(self, "错误", "请填写正确的Git仓库路径")
            return
        local_path = self.local_path_edit.text()
        if not local_path:
            QMessageBox.warning(self, "错误", "请填写local仓库路径")
            return
        try:
            repo = Repo(self.local_path_edit.text())
            g = repo.git
            g.fetch()
            self.textEdit.setText(g.diff("HEAD"))
            QMessageBox.information(self, "信息", "成功")
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mygitlab = MyGitlab()
    sys.exit(app.exec())
    # git@github.com:14045233/Python.git
