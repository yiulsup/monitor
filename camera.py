from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QThread
from PyQt5 import uic
import sys
import serial
import numpy as np 
import os
import time
import threading
import signal
import time
import binascii
import queue
import cv2

class vision(QThread):
    def __init__(self, cap, vision_widget):
        super().__init__()
        self.cap = cap
        self.vision_widget = vision_widget

    def run(self):
        while True:
            ret, frame = self.cap.read()
            frame = cv2.resize(frame, (640, 480))
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            qpixmap = QPixmap.fromImage(convert_to_Qt_format)
            self.vision_widget.setPixmap(qpixmap)
            self.vision_widget.show()

class monitor(QMainWindow):
    def __init__(self):
        super(monitor, self).__init__()
        uic.loadUi("camera.ui", self)
        self.show()
        
        self.cap = cv2.VideoCapture("/dev/video0")

        self.tVision = vision(self.cap, self.vision)
        self.tVision.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = monitor()
    window.show()
    sys.exit(app.exec_())