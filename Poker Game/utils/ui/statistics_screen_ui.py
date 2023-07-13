# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
"backround-size:cover;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.winner_btn = QtWidgets.QPushButton(self.centralwidget)
        self.winner_btn.setGeometry(QtCore.QRect(22, 34, 159, 45))
        self.winner_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.winner_btn.setFont(font)
        self.winner_btn.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.winner_btn.setObjectName("winner_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 182, 937, 463))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Summary_Table = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(120)
        sizePolicy.setHeightForWidth(self.Summary_Table.sizePolicy().hasHeightForWidth())
        self.Summary_Table.setSizePolicy(sizePolicy)
        self.Summary_Table.setMinimumSize(QtCore.QSize(0, 0))
        self.Summary_Table.setMaximumSize(QtCore.QSize(800, 2400))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Summary_Table.setFont(font)
        self.Summary_Table.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"")
        self.Summary_Table.setObjectName("Summary_Table")
        self.Summary_Table.setColumnCount(4)
        self.Summary_Table.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Summary_Table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Summary_Table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Summary_Table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Summary_Table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Summary_Table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Summary_Table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Summary_Table.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_2.addWidget(self.Summary_Table)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cards_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cards_input.setFont(font)
        self.cards_input.setStyleSheet("background-color: rgba(217, 217, 217, 66);\n"
"border-radius:3px;\n"
"")
        self.cards_input.setText("")
        self.cards_input.setObjectName("cards_input")
        self.horizontalLayout.addWidget(self.cards_input)
        self.cards_submit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cards_submit_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cards_submit_btn.setFont(font)
        self.cards_submit_btn.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.cards_submit_btn.setObjectName("cards_submit_btn")
        self.horizontalLayout.addWidget(self.cards_submit_btn)
        self.best_hands_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.best_hands_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.best_hands_btn.setFont(font)
        self.best_hands_btn.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.best_hands_btn.setObjectName("best_hands_btn")
        self.horizontalLayout.addWidget(self.best_hands_btn)
        self.Worst_Hands = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Worst_Hands.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Worst_Hands.setFont(font)
        self.Worst_Hands.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.Worst_Hands.setObjectName("Worst_Hands")
        self.horizontalLayout.addWidget(self.Worst_Hands)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.winner_btn.setText(_translate("MainWindow", "Winner_Screen"))
        item = self.Summary_Table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Summary_Table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.Summary_Table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.Summary_Table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.Summary_Table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.Summary_Table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.Summary_Table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.Summary_Table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.Summary_Table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.Summary_Table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.Summary_Table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.Summary_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cards"))
        item = self.Summary_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total Games"))
        item = self.Summary_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Win Games"))
        item = self.Summary_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Win_Rate"))
        self.cards_submit_btn.setText(_translate("MainWindow", "Submit"))
        self.best_hands_btn.setText(_translate("MainWindow", "Best Hands"))
        self.Worst_Hands.setText(_translate("MainWindow", "Worst Hands"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
