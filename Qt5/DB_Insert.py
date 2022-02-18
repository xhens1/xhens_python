import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QApplication, QLineEdit, QComboBox, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from numpy import place
import DBConnect

class InsertData(QWidget):

    def __init__(self, parent=None):
        super(InsertData, self).__init__(parent)
        self.name = []
        self.initUI()
        self.place = insert_place()
        self.place.signal.connect(self.place_trans)

    def initUI(self):
        Label1 = QLabel("이름 : ", self)
        Label2 = QLabel("위치 : ", self)
        Label3 = QLabel("설명 : ", self)
        self.Label4 = QLabel("", self)

        self.txt1 = QLineEdit(self)
        self.txt2 = QLineEdit(self)
        self.txt3 = QPlainTextEdit(self)

        self.btn1 = QPushButton("추가하기", self)     
        self.btn2 = QPushButton("돌아가기", self)      
        self.btn3 = QPushButton("위치 선택", self)      

        self.txt2.setReadOnly(True)

        self.txt1.setFixedSize(440, 25)
        self.txt2.setFixedSize(350, 25)
        self.txt3.setFixedSize(500, 300)

        Label1.move(20, 20)
        Label2.move(20, 60)
        Label3.move(20, 100)
        self.Label4.setVisible(False)

        self.txt1.move(80, 20)
        self.txt2.move(80, 60)
        self.txt3.move(20, 140)

        self.btn1.move(437, 450)
        self.btn1.clicked.connect(self.btnInsert)
        self.btn2.move(337, 450)
        self.btn2.clicked.connect(self.btnAction)
        self.btn3.move(440, 60)
        self.btn3.clicked.connect(self.btnplace)

        self.resize(540, 500)
        self.setWindowTitle('검색기')

        combo = DBConnect.init_name()
        for i in range(len(combo)):
            self.name.append(combo[i][0])

    def btnInsert(self, event):

        if self.txt1.text() in self.name:
            QMessageBox.about(self, "에러", "이름이 중복입니다.")
        elif self.txt1.text() == "" or self.txt2.text() == "" or self.txt3.toPlainText() == "":
            QMessageBox.about(self, "에러", "모든 값을 입력해주세요.")
        else:
            print(self.Label4.text())
            DBConnect.insert_attack(self.txt1.text(), self.txt3.toPlainText(), self.Label4.text())
            self.close()

    def btnAction(self, event):
        self.close()

    def btnplace(self, event):
        self.place.show()

    @pyqtSlot(int, str)
    def place_trans(self, tvalue, place):
        if self.txt2.text() == "":
            self.txt2.setText(place)
            self.Label4.setText(str(tvalue))
        else:
            checking = self.txt2.text().split(", ")
            select = False
            for i in range(len(checking)):
                if checking[i] == place:
                    select = True
                    QMessageBox.about(self, "에러", "중복된 대상을 선택하였습니다.")
                    break
            if select == False:
                self.txt2.setText(self.txt2.text() + ", " + place)
                self.Label4.setText(self.Label4.text() + ", " + str(tvalue))
        print(self.Label4.text())


#대상 선택
class insert_place(QWidget):
    signal = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(insert_place, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.data = []
        self.data.clear()
        Label1 = QLabel("위치 선택 : ",self)

        self.txt1 = QComboBox(self)
        self.txt2 = QLineEdit(self)

        self.btn1 = QPushButton("선택하기", self)

        self.txt1.setFixedSize(430, 25)
        self.txt2.setFixedSize(430, 25)

        Label1.move(20, 20)

        self.txt1.move(90, 20)
        self.txt2.move(90, 60)
        self.btn1.move(440,100)

        self.txt2.setReadOnly(True)

        combo = DBConnect.init_place()
        for i in range(len(combo)):
            self.txt1.addItem(combo[i][1])
            self.data.append(combo[i][0])

        self.txt1.addItem("기타")
        self.txt2.setText(self.txt1.currentText())
        self.txt1.currentIndexChanged.connect(self.ComboAction)
        self.btn1.clicked.connect(self.BtnAction)

    def ComboAction(self, event):
        if self.txt1.currentText() == "기타":
            self.txt2.setText("")
            self.txt2.setFocus()
            self.txt2.setReadOnly(False)
        else:
            self.txt2.setText(self.txt1.currentText())
            self.txt2.setReadOnly(True)

    #선택 버튼
    def BtnAction(self):
        if self.txt1.currentText() == "기타":
            if self.txt1.findText(self.txt2.text()) != -1:
                QMessageBox.about(self, "에러", "이름이 중복값입니다.")
            else:
                DBConnect.insert_place(self.txt2.text())
                combo = DBConnect.init_place()
                txtval = self.txt2.text()
                tt = combo[len(combo) - 1][0]
                self.signal.emit(tt, txtval)
                self.close()

        else:
            txtval = self.txt2.text()
            tt = self.data[self.txt1.currentIndex()]
            self.signal.emit(tt, txtval)
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InsertData()
    window.show()
    print(app)
    sys.exit(app.exec_())

