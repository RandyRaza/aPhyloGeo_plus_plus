# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pathlib
#from help import Ui_how_to_use
from parameters import Ui_Dialog
from help import Ui_how_to_use
#from cltree import Ui_ct 
import PyPDF2
import toytree
import toyplot.pdf

class Ui_MainWindow(object):
    

    def useWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_how_to_use()
        self.ui.setupUi(self.window)
        self.window.show()

    def param_Win(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1109, 981)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/archive (2)/sherbrooke.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../icons/archive (2)/sherbrooke.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../icons/archive (2)/sherbrooke.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../icons/archive (2)/sherbrooke.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../icons/archive (2)/sherbrooke.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../icons/archive (2)/sherbrooke.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(-10, 0, 1131, 91))
        self.top_frame.setStyleSheet("\n"
"background-color: rgb(222, 221, 218);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_frame.setObjectName("top_frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.top_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 10, 101, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setToolTip("Genetic Data")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../aPhyloGeo_plus_plus/aPhyloGeo_plus_plus/img/Genetic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(75, 75))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.top_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 10, 81, 71))
        self.pushButton_3.setToolTip("Climatic Data")
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../aPhyloGeo_plus_plus/aPhyloGeo_plus_plus/img/climatic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(75, 75))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.top_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 10, 81, 71))
        self.pushButton_4.setToolTip("Results")
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../aPhyloGeo_plus_plus/aPhyloGeo_plus_plus/img/result.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.top_frame)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 311, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../img/WSiN0h01.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.top_frame, clicked = lambda: self.useWindow())
        self.pushButton_11.setGeometry(QtCore.QRect(1000, 0, 111, 81))
        self.pushButton_11.setToolTip("How to use the application")
        self.pushButton_11.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-30, 90, 1151, 1100))
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.main_frame = QtWidgets.QFrame(self.page)
        self.main_frame.setEnabled(True)
        self.main_frame.setGeometry(QtCore.QRect(20, 0, 1131, 941))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.Gen_frame = QtWidgets.QFrame(self.main_frame)
        self.Gen_frame.setGeometry(QtCore.QRect(0, -10, 1121, 901))
        self.Gen_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Gen_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Gen_frame.setLineWidth(0)
        self.Gen_frame.setObjectName("Gen_frame")
        self.pushButton_6 = QtWidgets.QPushButton(self.Gen_frame, clicked = lambda: self.press_it())
        self.pushButton_6.setGeometry(QtCore.QRect(30, 30, 71, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../img/Browse.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Gen_frame, clicked = lambda: self.clear_it())
        self.pushButton_7.setGeometry(QtCore.QRect(30, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../img/erase.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit = QtWidgets.QTextEdit(self.Gen_frame)
        self.textEdit.setGeometry(QtCore.QRect(240, 30, 821, 181))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.Gen_frame)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 240, 821, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.Gen_frame)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 101, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Gen_frame)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 101, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.Gen_frame)
        self.pushButton_12.setGeometry(QtCore.QRect(40, 220, 61, 71))
        self.pushButton_12.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../img/seq.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon7)
        self.pushButton_12.setIconSize(QtCore.QSize(60, 70))
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_5 = QtWidgets.QLabel(self.Gen_frame)
        self.label_5.setGeometry(QtCore.QRect(110, 240, 67, 17))
        self.label_5.setObjectName("label_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.Gen_frame)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 310, 71, 71))
        self.pushButton_13.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../img/analytics.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_7 = QtWidgets.QLabel(self.Gen_frame)
        self.label_7.setGeometry(QtCore.QRect(110, 340, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.Gen_frame)
        self.label_11.setGeometry(QtCore.QRect(80, 620, 161, 71))
        self.label_11.setObjectName("label_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.Gen_frame)
        self.textBrowser.setGeometry(QtCore.QRect(240, 440, 821, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label_12 = QtWidgets.QLabel(self.Gen_frame)
        self.label_12.setGeometry(QtCore.QRect(90, 720, 67, 17))
        self.label_12.setObjectName("label_12")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Gen_frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(240, 650, 821, 191))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setEnabled(True)
        self.page_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.page_2.setObjectName("page_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(20, 0, 1121, 871))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.pressit())
        self.pushButton_8.setGeometry(QtCore.QRect(30, 30, 81, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.clear_cl())
        self.pushButton_9.setGeometry(QtCore.QRect(40, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(290, 270, 711, 181))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 50, 111, 41))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 150, 101, 31))
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(290, 50, 711, 181))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 230, 91, 91))
        self.pushButton_14.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../img/draw climatic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon9)
        self.pushButton_14.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(110, 240, 91, 81))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(50, 380, 67, 31))
        self.label_13.setObjectName("label_13")
        self.label_13.setToolTip("Choose chart type")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(40, 430, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 510, 261, 141))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 70, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 141, 31))
        self.label_16.setObjectName("label_16")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_3.setGeometry(QtCore.QRect(320, 480, 681, 192))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(590, 560, 67, 17))
        self.label_17.setObjectName("label_17")
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.graphicsView.raise_()
        self.textEdit_3.raise_()
        self.pushButton_14.raise_()
        self.label_10.raise_()
        self.label_13.raise_()
        self.comboBox.raise_()
        self.frame_3.raise_()
        self.graphicsView_3.raise_()
        self.label_17.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(20, 0, 1121, 891))
        self.frame_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.param_Win())
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 81, 61))
        self.pushButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../img/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon10)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 150, 71, 61))
        self.pushButton_10.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../img/submit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon11)
        self.pushButton_10.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(300, 270, 631, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tableView = QtWidgets.QTableView(self.frame_2)
        self.tableView.setGeometry(QtCore.QRect(300, 40, 631, 192))
        self.tableView.setObjectName("tableView")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(110, 70, 81, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(110, 160, 67, 21))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(510, 140, 241, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(120, 380, 121, 51))
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontit = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../icons/bImXxf01.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontit.setIcon(icon12)
        self.actiontit.setObjectName("actiontit")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(self.show_page) # type: ignore
        self.pushButton_3.clicked.connect(self.show_page_2) # type: ignore  (self.show_page2)
        self.pushButton_4.clicked.connect(self.show_page_3) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.comboBox.currentIndexChanged.connect(self.show_frame)
        self.frame_3.setHidden(True)
    def show_frame(self, value):
        if value is not None:
            self.frame_3.setHidden(False)
        else:
            self.frame_3.setHidden(True)

    def show_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def show_page_2(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_page_3(self):
        self.stackedWidget.setCurrentIndex(2)

        
    def press_it(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, "r") as f:
                content = f.read()
                self.textEdit.setText(content)
                global sequence
                sequence = ''
                for char in content:
                    sequence += char.strip()
                self.child_window = QtWidgets.QMainWindow()
                self.ui = Ui_how_to_use()
                self.ui.setupUi(self.child_window)
                self.child_window.setWindowModality(QtCore.Qt.NonModal)

        def color_background(letter):
            if letter == 'A':
                return 'background-color: yellow'
            elif letter == 'C':
                return 'background-color: blue'
            elif letter == 'G':
                return 'background-color: red'
            elif letter == 'T':
                return 'background-color: orange'
            else:
                return ''

        if 'sequence' in globals():
            formatted_sequence = ''.join(f'<span style="{color_background(l)}">{l}</span>' for l in sequence)
            self.textEdit.setText(formatted_sequence)


    def pressit(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, "r") as c:
                lines = c.readlines()
                num_rows = len(lines)
                first_line = lines[1].split(",")
                num_columns = len(first_line)
                cursor = QtGui.QTextCursor(self.textEdit_3.textCursor())
                cursor.insertTable(num_rows, num_columns)
                for line in lines:
                    line_split = line.split(",")
                    for value in line_split:
                        cursor.insertText(value)
                        cursor.movePosition(QtGui.QTextCursor.NextCell)
                self.child_window = QtWidgets.QMainWindow()
                self.ui = Ui_how_to_use()
                self.ui.setupUi(self.child_window)
                self.child_window.setWindowModality(QtCore.Qt.NonModal)
                #self.child_window.show()


    def prevent_closing(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, "r") as f:
                data = f.read()
                self.page.setText(data)
                self.child_window = QtWidgets.QMainWindow()
                self.ui = Ui_how_to_use()
                self.ui.setupUi(self.child_window)
                self.child_window.setWindowModality(QtCore.Qt.NonModal)
                self.child_window.show()    




    # press the button to delet data
    def clear_it(self):
        self.textEdit.clear()
    def clear_cl(self):
        self.textEdit_3.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Down"))
        self.label_2.setText(_translate("MainWindow", "File Browser"))
        self.label_3.setText(_translate("MainWindow", "Clear"))
        self.label_5.setText(_translate("MainWindow", "Seq_Alig"))
        self.label_7.setText(_translate("MainWindow", "Statistics"))
        self.label_11.setText(_translate("MainWindow", "matrix"))
        self.label_12.setText(_translate("MainWindow", "tree"))
        self.label.setText(_translate("MainWindow", "File Browser"))
        self.label_4.setText(_translate("MainWindow", "Clear"))
        self.label_10.setText(_translate("MainWindow", "      Draw \n"
"Climatic Tree"))
        self.label_13.setText(_translate("MainWindow", "Statistics"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bar Chart"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Line Chart"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Pie Chart"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Area Chart"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Scatter Chart"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Temperature"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Wind"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Humidity"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Altitude"))
        self.label_16.setText(_translate("MainWindow", "  Climate condition"))
        self.label_17.setText(_translate("MainWindow", "Map"))
        self.label_8.setText(_translate("MainWindow", "Settings"))
        self.label_9.setText(_translate("MainWindow", "Submit"))
        self.label_14.setText(_translate("MainWindow", "table of result in csv file"))
        self.label_15.setText(_translate("MainWindow", "Statistics==>"))
        self.actiontit.setText(_translate("MainWindow", "tit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
