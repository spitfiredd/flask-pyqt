import sys
from PyQt5 import QtWidgets
import requests


class FlaskyFrontEnd(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.lbl_a = QtWidgets.QLabel(self)
        self.lbl_a.setText("Number A")
        self.lbl_a.move(20, 20)

        self.lbl_b = QtWidgets.QLabel(self)
        self.lbl_b.setText("Number B")
        self.lbl_b.move(20, 45)

        self.textbox_a = QtWidgets.QLineEdit(self)
        self.textbox_a.move(100, 20)
        self.textbox_a.resize(100, 20)

        self.textbox_b = QtWidgets.QLineEdit(self)
        self.textbox_b.move(100, 45)
        self.textbox_b.resize(100, 20)

        self.button = QtWidgets.QPushButton('Calc', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        val_a, val_b = self.textbox_a.text(), self.textbox_b.text()
        url = "http://localhost:5000/adder/{}/{}".format(val_a, val_b)
        r = requests.get(url)
        json = r.json()
        answer = json['calc']
        QtWidgets.QMessageBox.question(
            self,
            "Message",
            "Answer: {}".format(str(answer)),
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )
        self.textbox_a.setText("")
        self.textbox_b.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = FlaskyFrontEnd()
    sys.exit(app.exec_())
