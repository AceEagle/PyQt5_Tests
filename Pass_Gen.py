import random
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

def PassGen(qte, symbs):
    Pass = 0
    numb = '9'
    bnumb = 10
    if qte < 1:
        raise TypeError

    elif qte < 2:
        Pass = random.randrange(0,9)
        return Pass

    else:
        RealNumb = float(numb * qte)
        BeforeNumb = '0'
        RealBeforeNumb = float('1' + BeforeNumb * (qte-1))
        Pass = random.randrange(RealBeforeNumb, RealNumb)
        return Pass

print(PassGen(6, 1))

class Pass_Gen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.numbs = QtWidgets.QSpinBox()

    if __name__ == "__main__":
        app = QtWidgets.QApplication([])

        widget = Pass_Gen()
        widget.resize(800, 600)
        widget.show()

        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Pass_Gen()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())

