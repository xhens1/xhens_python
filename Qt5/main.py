from email.charset import QP
import sys
from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QApplication
from Seacrch import Serach_Window
from Insert import InserData

class Main_Menubar(QWidget):
    def __init__(self):
        super(Main_Menubar, self).__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Serach", self)
        btn2 = QPushButton("Add")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Menubar()
    window.show()
    print(app)
    sys.exit(app.exec_())