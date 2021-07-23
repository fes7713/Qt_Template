
#######################
# Signal and slot
#######################
import time
from PyQt5.QtCore import Qt

class Ui_Functions():
    def __init__(self, window):
        self.window = window
        self.ui = window.ui

        ########################
        # Declare Variables#####
        ########################
        self.ui.password = ""


        ################################################
        # Connect Event Signals to Slots(Functions) ####
        ################################################
        self.ui.button_1.clicked.connect(lambda: self.update_pass(1))
        self.ui.button_2.clicked.connect(lambda: self.update_pass(2))
        self.ui.button_3.clicked.connect(lambda: self.update_pass(3))
        self.ui.button_4.clicked.connect(lambda: self.update_pass(4))
        self.ui.button_5.clicked.connect(lambda: self.update_pass(5))
        self.ui.button_6.clicked.connect(lambda: self.update_pass(6))
        self.ui.button_7.clicked.connect(lambda: self.update_pass(7))
        self.ui.button_8.clicked.connect(lambda: self.update_pass(8))
        self.ui.button_9.clicked.connect(lambda: self.update_pass(9))
        self.ui.button_0.clicked.connect(lambda: self.update_pass(0))
        self.ui.button_ok.clicked.connect(self.mousePressEvent)


        self.ui.display_line.setText("CODE32")

    #######################
    # functions for slots
    #######################
    def update_pass(self, num):
        self.ui.password += str(num)
        print(self.ui.password)
        self.ui.display_line.setText("*"*len(self.ui.password))

    def mousePressEvent(self):
        if self.ui.password == "Unlocked":
            self.window.close()
        if self.ui.password != "" and int("CODE", 32) == int(self.ui.password):
            self.ui.password = "Unlocked"
            self.ui.display_line.setText("104.236.86.11")
            self.ui.button_ok.setText("close")
            print(self.ui.display_line.text())

        else:
            self.ui.password = ""
            self.ui.display_line.setText("Incorrect passcode")

    ########################
    # Key Setting (ASCII)###
    ########################
    def key_event(self, event):
        # event.key() to get keyboard input
        print(event.key())
        key = event.key()
        if 48 <= key <= 57:
            self.update_pass(int(chr(key)))

        # 16777220 is Enter key code
        if key == 16777220:
            self.mousePressEvent()

