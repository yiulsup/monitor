from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QThread
from PyQt5 import uic
import sys
import serial
import numpy as np 
import os
import serial
import cv2
import sys
import time
import threading
import signal
import time
import binascii
import queue

class radar(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            pass


class thermal(QThread):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        while True:
            pass    



class monitor(QMainWindow):
    def __init__(self):
        super(monitor, self).__init__()
        uic.loadUi("monitor.ui", self)
        self.show()
        self.tRadar = radar()
        self.mRadar.start()
        self.tThermal = thermal()
        self.tThermal.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = monitor()
    window.show()
    sys.exit(app.exec_())