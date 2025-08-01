import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout

# 定义一个类，继承QWidget。这是万法之宗，是基础。
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        widget = QWidget()
        widget.resize(800, 600)
        widget.setWindowTitle('《红尘证道录》Ver 0.0.1')
        self.init_ui()


    def init_ui(self):
        # 先来个标签，提示用户输入道号。
        label_dao_hao = QLabel('请输入您的道号：', self)
        # 然后是输入框
        self.input_dao_hao = QLineEdit(self)
        # 最后是按钮
        self.btn_enter = QPushButton('开始修行之路', self)

        # 栅格布局
        layout = QGridLayout()
        layout.addWidget(label_dao_hao, 0, 0)
        layout.addWidget(self.input_dao_hao, 0, 1)
        layout.addWidget(self.btn_enter, 1, 0, 1, 2)

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    LoginWindo = LoginWindow()

    LoginWindo.show()
    sys.exit(app.exec_())