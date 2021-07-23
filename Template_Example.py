from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(116, 72)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("Label")
        self.pushButton.setText("Push Button")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(main)
    main.show()

    sys.exit(app.exec_())
