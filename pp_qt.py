import sys

from PyQt5.QtGui import QFont

from partikel_qt_res import *
from texts import Texts


class MeinDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.gs = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.gs)
        self.ctimer = QtCore.QTimer()
        self.ctimer.start(1)
        self.ctimer.timeout.connect(self.constantUpdate)

        self.textindex = 0
        self.text = Texts().getTexts()
        self.res = None

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.res is not None:
            self.gs.removeItem(self.res)
        self.res = self.gs.addText(self.text[self.textindex], QFont("Courier", 30))
        #self.res.setTextWidth(1000)
        qp.end()

    def mousePressEvent(self, event):
        button = event.button()
        if button == 1:  # left
            if self.textindex == (len(self.text) - 1):
                pass
            else:
                self.textindex += 1
        elif button == 2:  # right
            if self.textindex == 0:
                pass
            else:
                self.textindex -= 1

    def constantUpdate(self):
        self.update()


app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())
