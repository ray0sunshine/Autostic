import threading
import sys
import time

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from utilContext import *
from utilPrimitive import *

import random

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(250,500)
        self.move(cd.winX, cd.winY + 30)

        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop)
        QWidget.setLayout(self, self.vbox)

        self.font = QFont('Arial', 12, 2)
        self.style = 'color: yellow'

        self.timeLabel = self.addLabel(str(time.ctime()))
        self.progLabel = self.addLabel('Progress: ' + str(cd.runsDone) + ' / ' + str(cd.runsLimit))
        self.trashLabel = self.addLabel('Burnt fodder: ' + str(cd.burnFodder) + ' / ' + str(cd.burnFodderLimit))
        self.repairLabel = self.addLabel('Repair skipped: ' + str(cd.repairSkip) + ' / ' + str(cd.repairSkipLimit))
        self.runtimeLabel = self.addLabel('Runtime: ???')
        self.logiLabel = self.addLabel('Logistic running: ' + str(cd.LOGISTIC_RUNNING))
        self.mapLabel = self.addLabel('Map running: ' + str(cd.MAP_RUNNING))
        self.orderLabel = self.addLabel('First order: ' + str(cd.firstOrder))
        self.threadLabel = self.addLabel(self.threadStr())
        self.logiTimeLabel = self.addLabel(self.logiStr())

        self.startTimer()

    def addLabel(self, text):
        label = QLabel()
        label.setText(text)
        label.setStyleSheet(self.style)
        label.setFont(self.font)
        self.vbox.addWidget(label)
        return label

    def updateLabels(self):
        self.timeLabel.setText(str(time.ctime()))
        self.progLabel.setText('Progress: ' + str(cd.runsDone) + ' / ' + str(cd.runsLimit))
        self.trashLabel.setText('Burnt fodder: ' + str(cd.burnFodder) + ' / ' + str(cd.burnFodderLimit))
        self.repairLabel.setText('Repair skipped: ' + str(cd.repairSkip) + ' / ' + str(cd.repairSkipLimit))
        self.logiLabel.setText('Logistic running: ' + str(cd.LOGISTIC_RUNNING))
        if cd.MAP_RUNNING:
            timeDelta = time.time() - cd.RUNTIME
            self.runtimeLabel.setText('Runtime: ' + str(round(timeDelta)) + 's (' + str(round(timeDelta/60, 1)) + ' min)')
        self.mapLabel.setText('Map running: ' + str(cd.MAP_RUNNING))
        self.orderLabel.setText('First order: ' + str(cd.firstOrder))
        self.threadLabel.setText(self.threadStr())
        self.logiTimeLabel.setText(self.logiStr())

    def threadStr(self):
        ret = 'Thread count: ' + str(threading.activeCount())
        ret += '\n' + '\n'.join(['[thread]: ' + thread.name for thread in threading.enumerate()])
        return ret

    def logiStr(self):
        ret = 'logistics:'
        for ct in cd.logiCountdown:
            if ct == None:
                ret += '\nlogi(s): ???'
            else:
                ret += '\nlogi(s): ' + str(round(ct - time.time())) + 's (' + str(round((ct - time.time())/60, 1)) + ' min)'
        ret += '\nWaiting Logs: ' + str(cd.logiWait)
        return ret

    def startTimer(self):
        timer = QTimer(self)
        timer.setSingleShot(False)
        timer.timeout.connect(self.update)
        timer.start(40)

    def paintEvent(self, e):
        bushido()
        self.updateLabels()
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(0,0,0,128))
        qp.drawRect(0,0,250,500)
        qp.end()

def uiThread():
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    app.exec_()

def initUI():
    ui = threading.Thread(None, uiThread, 'ui')
    ui.start()
