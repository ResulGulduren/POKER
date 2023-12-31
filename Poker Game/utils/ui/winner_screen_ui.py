# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winner_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import utils.ui.poker_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 785)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 785))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 785))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 785))
        self.centralwidget.setMaximumSize(QtCore.QSize(1600, 785))
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "\n"
                                         "background-color: rgb(12, 142, 10);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.p2_name = QtWidgets.QLabel(self.centralwidget)
        self.p2_name.setGeometry(QtCore.QRect(460, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.p2_name.setFont(font)
        self.p2_name.setStyleSheet("")
        self.p2_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_name.setObjectName("p2_name")
        self.p2_card1 = QtWidgets.QLabel(self.centralwidget)
        self.p2_card1.setGeometry(QtCore.QRect(440, 65, 71, 116))
        self.p2_card1.setStyleSheet("border-radius: 5px;")
        self.p2_card1.setText("")
        self.p2_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p2_card1.setScaledContents(True)
        self.p2_card1.setObjectName("p2_card1")
        self.p2_card2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_card2.setGeometry(QtCore.QRect(535, 65, 71, 116))
        self.p2_card2.setStyleSheet("border-radius: 5px;")
        self.p2_card2.setText("")
        self.p2_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p2_card2.setScaledContents(True)
        self.p2_card2.setObjectName("p2_card2")
        self.p3_card2 = QtWidgets.QLabel(self.centralwidget)
        self.p3_card2.setGeometry(QtCore.QRect(1090, 65, 71, 116))
        self.p3_card2.setStyleSheet("border-radius: 5px;")
        self.p3_card2.setText("")
        self.p3_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p3_card2.setScaledContents(True)
        self.p3_card2.setObjectName("p3_card2")
        self.p3_name = QtWidgets.QLabel(self.centralwidget)
        self.p3_name.setGeometry(QtCore.QRect(1015, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.p3_name.setFont(font)
        self.p3_name.setStyleSheet("")
        self.p3_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p3_name.setObjectName("p3_name")
        self.p3_card1 = QtWidgets.QLabel(self.centralwidget)
        self.p3_card1.setGeometry(QtCore.QRect(995, 65, 71, 116))
        self.p3_card1.setStyleSheet("border-radius: 5px;")
        self.p3_card1.setText("")
        self.p3_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p3_card1.setScaledContents(True)
        self.p3_card1.setObjectName("p3_card1")
        self.p5_card2 = QtWidgets.QLabel(self.centralwidget)
        self.p5_card2.setGeometry(QtCore.QRect(1090, 605, 71, 116))
        self.p5_card2.setStyleSheet("border-radius: 5px;")
        self.p5_card2.setText("")
        self.p5_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p5_card2.setScaledContents(True)
        self.p5_card2.setObjectName("p5_card2")
        self.p5_name = QtWidgets.QLabel(self.centralwidget)
        self.p5_name.setGeometry(QtCore.QRect(1015, 720, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.p5_name.setFont(font)
        self.p5_name.setStyleSheet("")
        self.p5_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p5_name.setObjectName("p5_name")
        self.p5_card1 = QtWidgets.QLabel(self.centralwidget)
        self.p5_card1.setGeometry(QtCore.QRect(995, 605, 71, 116))
        self.p5_card1.setStyleSheet("border-radius: 5px;")
        self.p5_card1.setText("")
        self.p5_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p5_card1.setScaledContents(True)
        self.p5_card1.setObjectName("p5_card1")
        self.p6_card2 = QtWidgets.QLabel(self.centralwidget)
        self.p6_card2.setGeometry(QtCore.QRect(535, 605, 71, 116))
        self.p6_card2.setStyleSheet("border-radius: 5px;")
        self.p6_card2.setText("")
        self.p6_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p6_card2.setScaledContents(True)
        self.p6_card2.setObjectName("p6_card2")
        self.p6_name = QtWidgets.QLabel(self.centralwidget)
        self.p6_name.setGeometry(QtCore.QRect(460, 720, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.p6_name.setFont(font)
        self.p6_name.setStyleSheet("")
        self.p6_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p6_name.setObjectName("p6_name")
        self.p6_card1 = QtWidgets.QLabel(self.centralwidget)
        self.p6_card1.setGeometry(QtCore.QRect(440, 605, 71, 116))
        self.p6_card1.setStyleSheet("border-radius: 5px;")
        self.p6_card1.setText("")
        self.p6_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p6_card1.setScaledContents(True)
        self.p6_card1.setObjectName("p6_card1")
        self.p1_card2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_card2.setGeometry(QtCore.QRect(170, 335, 71, 116))
        self.p1_card2.setStyleSheet("border-radius: 5px;")
        self.p1_card2.setText("")
        self.p1_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p1_card2.setScaledContents(True)
        self.p1_card2.setObjectName("p1_card2")
        self.p1_name = QtWidgets.QLabel(self.centralwidget)
        self.p1_name.setGeometry(QtCore.QRect(95, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.p1_name.setFont(font)
        self.p1_name.setStyleSheet("")
        self.p1_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_name.setObjectName("p1_name")
        self.p1_card1 = QtWidgets.QLabel(self.centralwidget)
        self.p1_card1.setGeometry(QtCore.QRect(75, 335, 71, 116))
        self.p1_card1.setStyleSheet("border-radius: 5px;")
        self.p1_card1.setText("")
        self.p1_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p1_card1.setScaledContents(True)
        self.p1_card1.setObjectName("p1_card1")
        self.p4_card2 = QtWidgets.QLabel(self.centralwidget)
        self.p4_card2.setGeometry(QtCore.QRect(1455, 335, 71, 116))
        self.p4_card2.setStyleSheet("border-radius: 5px;")
        self.p4_card2.setText("")
        self.p4_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p4_card2.setScaledContents(True)
        self.p4_card2.setObjectName("p4_card2")
        self.p4_name = QtWidgets.QLabel(self.centralwidget)
        self.p4_name.setGeometry(QtCore.QRect(1380, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.p4_name.setFont(font)
        self.p4_name.setStyleSheet("")
        self.p4_name.setAlignment(QtCore.Qt.AlignCenter)
        self.p4_name.setObjectName("p4_name")
        self.p4_card1 = QtWidgets.QLabel(self.centralwidget)
        self.p4_card1.setGeometry(QtCore.QRect(1360, 335, 71, 116))
        self.p4_card1.setStyleSheet("border-radius: 5px;")
        self.p4_card1.setText("")
        self.p4_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.p4_card1.setScaledContents(True)
        self.p4_card1.setObjectName("p4_card1")
        self.desk_card1 = QtWidgets.QLabel(self.centralwidget)
        self.desk_card1.setGeometry(QtCore.QRect(575, 335, 71, 116))
        self.desk_card1.setStyleSheet("border-radius: 5px;")
        self.desk_card1.setText("")
        self.desk_card1.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.desk_card1.setScaledContents(True)
        self.desk_card1.setObjectName("desk_card1")
        self.desk_card2 = QtWidgets.QLabel(self.centralwidget)
        self.desk_card2.setGeometry(QtCore.QRect(670, 335, 71, 116))
        self.desk_card2.setStyleSheet("border-radius: 5px;")
        self.desk_card2.setText("")
        self.desk_card2.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.desk_card2.setScaledContents(True)
        self.desk_card2.setObjectName("desk_card2")
        self.desk_card3 = QtWidgets.QLabel(self.centralwidget)
        self.desk_card3.setGeometry(QtCore.QRect(765, 335, 71, 116))
        self.desk_card3.setStyleSheet("border-radius: 5px;")
        self.desk_card3.setText("")
        self.desk_card3.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.desk_card3.setScaledContents(True)
        self.desk_card3.setObjectName("desk_card3")
        self.desk_card4 = QtWidgets.QLabel(self.centralwidget)
        self.desk_card4.setGeometry(QtCore.QRect(860, 335, 71, 116))
        self.desk_card4.setStyleSheet("border-radius: 5px;")
        self.desk_card4.setText("")
        self.desk_card4.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.desk_card4.setScaledContents(True)
        self.desk_card4.setObjectName("desk_card4")
        self.desk_card5 = QtWidgets.QLabel(self.centralwidget)
        self.desk_card5.setGeometry(QtCore.QRect(955, 335, 71, 116))
        self.desk_card5.setStyleSheet("border-radius: 5px;")
        self.desk_card5.setText("")
        self.desk_card5.setPixmap(QtGui.QPixmap(":/icon/1B.png"))
        self.desk_card5.setScaledContents(True)
        self.desk_card5.setObjectName("desk_card5")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(266, 212, 1115, 113))
        self.gridWidget.setStyleSheet("background-color: rgb(204, 204, 204);\n"
                                      "\n"
                                      "")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(9, 2, 9, 2)
        self.gridLayout.setHorizontalSpacing(11)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.Royalflush_btn = QtWidgets.QPushButton(self.gridWidget)
        self.Royalflush_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Royalflush_btn.setFont(font)
        self.Royalflush_btn.setObjectName("Royalflush_btn")
        self.gridLayout.addWidget(self.Royalflush_btn, 0, 0, 1, 1)
        self.flush_straight_btn = QtWidgets.QPushButton(self.gridWidget)
        self.flush_straight_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flush_straight_btn.setFont(font)
        self.flush_straight_btn.setObjectName("flush_straight_btn")
        self.gridLayout.addWidget(self.flush_straight_btn, 0, 1, 1, 1)
        self.flush_btn = QtWidgets.QPushButton(self.gridWidget)
        self.flush_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flush_btn.setFont(font)
        self.flush_btn.setStyleSheet("background-color: rgb(204, 204, 204);\n"
                                     "\n"
                                     "")
        self.flush_btn.setObjectName("flush_btn")
        self.gridLayout.addWidget(self.flush_btn, 0, 4, 1, 1)
        self.higher_btn = QtWidgets.QPushButton(self.gridWidget)
        self.higher_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.higher_btn.setFont(font)
        self.higher_btn.setObjectName("higher_btn")
        self.gridLayout.addWidget(self.higher_btn, 1, 4, 1, 1)
        self.one_btn = QtWidgets.QPushButton(self.gridWidget)
        self.one_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.one_btn.setFont(font)
        self.one_btn.setObjectName("one_btn")
        self.gridLayout.addWidget(self.one_btn, 1, 3, 1, 1)
        self.straight_btn = QtWidgets.QPushButton(self.gridWidget)
        self.straight_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.straight_btn.setFont(font)
        self.straight_btn.setObjectName("straight_btn")
        self.gridLayout.addWidget(self.straight_btn, 1, 0, 1, 1)
        self.three_btn = QtWidgets.QPushButton(self.gridWidget)
        self.three_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.three_btn.setFont(font)
        self.three_btn.setObjectName("three_btn")
        self.gridLayout.addWidget(self.three_btn, 1, 1, 1, 1)
        self.two_btn = QtWidgets.QPushButton(self.gridWidget)
        self.two_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.two_btn.setFont(font)
        self.two_btn.setObjectName("two_btn")
        self.gridLayout.addWidget(self.two_btn, 1, 2, 1, 1)
        self.four_btn = QtWidgets.QPushButton(self.gridWidget)
        self.four_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.four_btn.setFont(font)
        self.four_btn.setObjectName("four_btn")
        self.gridLayout.addWidget(self.four_btn, 0, 2, 1, 1)
        self.full_button = QtWidgets.QPushButton(self.gridWidget)
        self.full_button.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.full_button.setFont(font)
        self.full_button.setObjectName("full_button")
        self.gridLayout.addWidget(self.full_button, 0, 3, 1, 1)
        self.label_playerturn = QtWidgets.QLabel(self.centralwidget)
        self.label_playerturn.setGeometry(QtCore.QRect(554, 478, 450, 110))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_playerturn.setFont(font)
        self.label_playerturn.setStyleSheet(
            "background-color: rgb(12, 142, 10);")
        self.label_playerturn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_playerturn.setObjectName("label_playerturn")
        self.label_p1bet = QtWidgets.QLabel(self.centralwidget)
        self.label_p1bet.setGeometry(QtCore.QRect(120, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_p1bet.setFont(font)
        self.label_p1bet.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "border-radius:20px;\n"
                                       "")
        self.label_p1bet.setText("")
        self.label_p1bet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_p1bet.setObjectName("label_p1bet")
        self.label_p2bet = QtWidgets.QLabel(self.centralwidget)
        self.label_p2bet.setGeometry(QtCore.QRect(480, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_p2bet.setFont(font)
        self.label_p2bet.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "border-radius:20px;\n"
                                       "")
        self.label_p2bet.setText("")
        self.label_p2bet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_p2bet.setObjectName("label_p2bet")
        self.label_p3bet = QtWidgets.QLabel(self.centralwidget)
        self.label_p3bet.setGeometry(QtCore.QRect(1040, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_p3bet.setFont(font)
        self.label_p3bet.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "border-radius:20px;\n"
                                       "")
        self.label_p3bet.setText("")
        self.label_p3bet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_p3bet.setObjectName("label_p3bet")
        self.label_p4bet = QtWidgets.QLabel(self.centralwidget)
        self.label_p4bet.setGeometry(QtCore.QRect(1400, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_p4bet.setFont(font)
        self.label_p4bet.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "border-radius:20px;\n"
                                       "")
        self.label_p4bet.setText("")
        self.label_p4bet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_p4bet.setObjectName("label_p4bet")
        self.label_p5bet = QtWidgets.QLabel(self.centralwidget)
        self.label_p5bet.setGeometry(QtCore.QRect(1040, 560, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_p5bet.setFont(font)
        self.label_p5bet.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "border-radius:20px;\n"
                                       "")
        self.label_p5bet.setText("")
        self.label_p5bet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_p5bet.setObjectName("label_p5bet")
        self.label_p6bet = QtWidgets.QLabel(self.centralwidget)
        self.label_p6bet.setGeometry(QtCore.QRect(480, 560, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_p6bet.setFont(font)
        self.label_p6bet.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "border-radius:20px;\n"
                                       "")
        self.label_p6bet.setText("")
        self.label_p6bet.setAlignment(QtCore.Qt.AlignCenter)
        self.label_p6bet.setObjectName("label_p6bet")
        self.two_winner_btn = QtWidgets.QPushButton(self.centralwidget)
        self.two_winner_btn.setGeometry(QtCore.QRect(722, 146, 159, 45))
        self.two_winner_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.two_winner_btn.setFont(font)
        self.two_winner_btn.setStyleSheet(
            "background-color: rgb(204, 204, 204);")
        self.two_winner_btn.setObjectName("two_winner_btn")
        self.statistics_btn = QtWidgets.QPushButton(self.centralwidget)
        self.statistics_btn.setGeometry(QtCore.QRect(1278, 588, 159, 45))
        self.statistics_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statistics_btn.setFont(font)
        self.statistics_btn.setStyleSheet(
            "background-color: rgb(204, 204, 204);")
        self.statistics_btn.setObjectName("statistics_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p2_name.setText(_translate("MainWindow", "P2"))
        self.p3_name.setText(_translate("MainWindow", "P3"))
        self.p5_name.setText(_translate("MainWindow", "P5"))
        self.p6_name.setText(_translate("MainWindow", "P6"))
        self.p1_name.setText(_translate("MainWindow", "P1"))
        self.p4_name.setText(_translate("MainWindow", "P4"))
        self.Royalflush_btn.setText(_translate("MainWindow", "Royal Flush"))
        self.flush_straight_btn.setText(
            _translate("MainWindow", "Straight Flush"))
        self.flush_btn.setText(_translate("MainWindow", "Flush"))
        self.higher_btn.setText(_translate("MainWindow", "Higher Card"))
        self.one_btn.setText(_translate("MainWindow", "One Pair"))
        self.straight_btn.setText(_translate("MainWindow", "Straight"))
        self.three_btn.setText(_translate("MainWindow", "Three Kind"))
        self.two_btn.setText(_translate("MainWindow", "Two Pair"))
        self.four_btn.setText(_translate("MainWindow", "Four Kind"))
        self.full_button.setText(_translate("MainWindow", "Full House"))
        self.label_playerturn.setText(_translate("MainWindow", "Winner"))
        self.two_winner_btn.setText(_translate("MainWindow", "Two winner"))
        self.statistics_btn.setText(_translate("MainWindow", "Statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
