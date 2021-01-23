import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Рисовать")

class Example(QMainWindow, UI_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.update()

    def paintEvent(self, event):
        self.nb = QPainter()
        self.nb.begin(self)
        a = random.randint(10, 250)
        self.nb.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.nb.drawEllipse(0, 0, a, a)
        self.nb.end()

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())