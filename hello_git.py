#这是我第一个git项目
from PyQt5.Qt import *

class Mywin(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello git")
        self.resize(600,400)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("按钮",self)
        btn.move(100,100)
        btn.clicked.connect(lambda :print("按钮被点击"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = Mywin()
    win.show()

    sys.exit(app.exec_())



