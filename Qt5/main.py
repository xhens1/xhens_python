from email.charset import QP
import sys
from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QApplication
from Search import Search_Window

class Main_Menubar(QWidget):
    def __init__(self):
        super(Main_Menubar, self).__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("찾기", self)
        btn2 = QPushButton("추가")

        btn1.clicked.connect(self.search)
        #추가 부분 추가 예정
        #

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(btn1)
        grid.addWidget(btn2)

        self.setWindowTitle("전국 명소 찾기")
        self.resize(300, 300)

    def search(self):
        self.Search_ = Search_Window()
        self.Search_.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Menubar()
    window.show()
    print(app)
    sys.exit(app.exec_())