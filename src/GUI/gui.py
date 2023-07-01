from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar


class GUI:
    def __init__(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        #sys.exit(self.app.exec_())
        self.app.exec_()

    def get_ui(self):
        return self.ui



class MyPaintWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.figure = plt.gcf()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.mpl_connect("button_press_event", self._on_left_click)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_xlim([1, 30])
        self.axes.set_ylim([1, 30])
        self.cities = []

        layout_canvas = QtWidgets.QVBoxLayout(self)
        layout_canvas.addWidget(self.canvas)

    def _on_left_click(self, event):
        x = event.xdata
        y = event.ydata
        self.axes.scatter(x, y, s=30)
        self.cities.append((x, y))
        self.figure.canvas.draw()

    def get_cities(self):
        return self.cities

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.lineEdit_X = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_X.setGeometry(QtCore.QRect(30, 40, 191, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_X.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("System")
        self.lineEdit_X.setFont(font)
        self.lineEdit_X.setObjectName("lineEdit_X")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 490, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.ready = 0

        self.sc = MyPaintWidget(self.centralwidget)
        self.sc.setGeometry(300, 10, 481, 531)
        self.sc.setObjectName("sc")

        self.lineEdit_X_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_X_2.setGeometry(QtCore.QRect(30, 110, 191, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_X_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_X_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("System")
        self.lineEdit_X_2.setFont(font)
        self.lineEdit_X_2.setObjectName("lineEdit_X_2")
        self.lineEdit_X_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_X_3.setGeometry(QtCore.QRect(30, 190, 191, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_X_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_X_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("System")
        self.lineEdit_X_3.setFont(font)
        self.lineEdit_X_3.setObjectName("lineEdit_X_3")
        self.lineEdit_X_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_X_4.setGeometry(QtCore.QRect(30, 280, 191, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_X_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_X_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("System")
        self.lineEdit_X_4.setFont(font)
        self.lineEdit_X_4.setObjectName("lineEdit_X_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TSP"))
        self.label.setText(_translate("MainWindow", "Размер популяции"))
        self.label_2.setText(_translate("MainWindow", "Количество поколений"))
        self.pushButton.setText(_translate("MainWindow", "Запустить алгоритм"))
        self.label_3.setText(_translate("MainWindow", "Вероятность мутации"))
        self.label_4.setText(_translate("MainWindow", "Вероятность кроссинговера"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.ready = 1