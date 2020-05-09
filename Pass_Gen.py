import random
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

app = QApplication([])

#yotoutlemonde
