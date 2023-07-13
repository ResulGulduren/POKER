import sqlite3

from PyQt5 import QtWidgets
from utils.ui.statistics_screen_ui import Ui_MainWindow


class StatisticsScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(StatisticsScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.winner_btn.clicked.connect(self.open_winner_screen)
        self.ui.cards_submit_btn.clicked.connect(self.search)
        self.ui.best_hands_btn.clicked.connect(self.best)
        self.ui.Worst_Hands.clicked.connect(self.worst)
    def open_winner_screen(self):
        from utils.winner_screen import WinnerScreen
        self.hide()
        self.winner_screen = WinnerScreen()
        self.winner_screen.show()
    
    
    
    def serch(self):
        self.ui.Summary_Table.clearContents()
        
        self.connect=sqlite3.connect('poker_statistic.db')
        self.cursor=self.connect.cursor()
        word=self.ui.cards_input.text()
        deel=word.split()
        wordt=word[2]+" "+ word[0]
        #print(wordt)
        self.cursor.execute('Select * From winners')
        data=self.cursor.fetchall()
        #print(data)
        new_data=[]
        for i in data:
           for j in i:
                if word in str(j) or wordt in str(j):
                    new_data.append(i)
                    break
        #print(new_data)
        for row ,form in enumerate(new_data):
            for column,item in enumerate(form):
                self.ui.Summary_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(item)))
                column+=1
            row_position=self.ui.Summary_Table.rowCount()
            self.ui.Summary_Table.insertRow(row_position)

    def search(self):
        self.ui.Summary_Table.clearContents()
    
        self.connect = sqlite3.connect('poker_statistic.db')
        self.cursor = self.connect.cursor()
        word = self.ui.cards_input.text()
        deel = word.split()
        wordt = " ".join(deel)  # Girilen girişi kelime listesinden geri dönüştürmek için birleştirme işlemi
    
        self.cursor.execute('SELECT * FROM winners')
        data = self.cursor.fetchall()

        new_data = []
        for i in data:
            for j in i:
                if word in str(j) or wordt in str(j):
                    new_data.append(i)
                    break

        for row, form in enumerate(new_data):
            self.ui.Summary_Table.insertRow(row)
            for column, item in enumerate(form):
                if isinstance(item, float):
                    item = "{:.3f}".format(item)  # Virgülden sonra 3 basamak görüntüleme
                self.ui.Summary_Table.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))

        self.connect.close()
    
    
    
    def best(self):
        self.connect=sqlite3.connect('poker_statistic.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('Select * From winners order by rate Desc Limit 10')
        data=self.cursor.fetchall()
        # print(data)
        for row ,form in enumerate(data):
            for column,item in enumerate(form):
                self.ui.Summary_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(item)))
                column+=1
            row_position=self.ui.Summary_Table.rowCount()
            self.ui.Summary_Table.insertRow(row_position)
    def worst(self):
        self.connect=sqlite3.connect('poker_statistic.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('Select * From winners order by rate Asc Limit 10')
        data=self.cursor.fetchall()
        # print(data)
        for row ,form in enumerate(data):
            for column,item in enumerate(form):
                self.ui.Summary_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(item)))
                column+=1
            row_position=self.ui.Summary_Table.rowCount()
            self.ui.Summary_Table.insertRow(row_position)