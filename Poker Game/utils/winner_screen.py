# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

from PyQt5 import QtWidgets, QtGui
from utils.ui.winner_screen_ui import Ui_MainWindow
from utils.winner_check import PokerGame
import random,sqlite3


class WinnerScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(WinnerScreen, self).__init__()
        self.screen = Ui_MainWindow()
        self.screen.setupUi(self)
        self.game = PokerGame()
        
        
        
        self.screen.statistics_btn.clicked.connect(self.open_statistics_screen)
        self.screen.two_winner_btn.clicked.connect(self.two_winner)
        self.screen.Royalflush_btn.clicked.connect(self.royal_flush)
        self.screen.flush_straight_btn.clicked.connect(self.flush_straight)
        self.screen.four_btn.clicked.connect(self.four_of_a_kind)
        self.screen.full_button.clicked.connect(self.full_house)
        self.screen.flush_btn.clicked.connect(self.flush)
        self.screen.straight_btn.clicked.connect(self.straight)
        self.screen.three_btn.clicked.connect(self.three_of_a_kind)
        self.screen.two_btn.clicked.connect(self.two_pair)
        self.screen.one_btn.clicked.connect(self.one_pair)
        self.screen.higher_btn.clicked.connect(self.higher_card)

    def two_winner(self):
        self.count = 0
        while True:
            self.game.start_game()
            self.count += 1
            if len(self.game.winner_list) > 2:
                self.show_winner()
                break
            self.game.restartGame()
        self.game.restartGame()

    def open_statistics_screen(self):
        from utils.statistics_screen import StatisticsScreen
        self.hide()
        self.statistics_screen = StatisticsScreen()
        self.statistics_screen.show()


    def database(self):
        connection = sqlite3.connect("poker_statistic.db")
        cursor = connection.cursor()

        # Kazananları güncelle
        for hand in self.game.winning_players:
            cursor.execute("SELECT * FROM winners WHERE hand = ?", (str(hand),))
            existing_hand = cursor.fetchone()

            if existing_hand is not None:
                total_games = existing_hand[1] + 1
                win_games = existing_hand[2] + 1
                win_rate = win_games / total_games
                cursor.execute(
                    "UPDATE winners SET total_games = ?, won_games = ?, rate = ? WHERE hand = ?",
                    (total_games, win_games, win_rate, str(hand)),
                )
            else:
                cursor.execute(
                    "INSERT INTO winners (hand, total_games, won_games, rate) VALUES (?, ?, ?, ?)",
                    (str(hand), 1, 1, 1.0),
                )

        # Kaybedenleri güncelle
        for hand in self.game.losing_players:
            cursor.execute("SELECT * FROM winners WHERE hand = ?", (str(hand),))
            existing_hand = cursor.fetchone()

            if existing_hand is not None:
                total_games = existing_hand[1] + 1
                win_games = existing_hand[2]
                win_rate = win_games / total_games
                cursor.execute(
                    "UPDATE winners SET total_games = ?, won_games = ?, rate = ? WHERE hand = ?",
                    (total_games, win_games, win_rate, str(hand)),
                )
            else:
                cursor.execute(
                    "INSERT INTO winners (hand, total_games, won_games, rate) VALUES (?, ?, ?, ?)",
                    (str(hand), 1, 0, 0.0),
                )

        connection.commit()
        connection.close()

        
        self.game.winning_players = []
        self.game.losing_players = []


    def winner_option(self):
        
        while True:
           
            self.count += 1
            
            if self.option == self.game.rank_names[self.game.number]:
                self.winner = self.game.find_winner(self.game.hand_evaluation)
                #print(self.winner)
                #print(self.game.playerstwocards)
                #print(self.game.community_cards)
                #print('Kaybedenler',self.game.losing_players)
                #print('Kazananlar',self.game.winning_players)
                if self.winner is not None:
                    self.show_winner()
                    self.database()
                else:
                    self.game = PokerGame()
                    
                    continue

                break
            self.game = PokerGame()

    
        
   
        

    def royal_flush(self):
        self.count = 0
        self.option = 'Royal Flush'
        self.winner_option()

    def flush_straight(self):
        self.count = 0
        self.option = 'Straight Flush'
        self.winner_option()

    def four_of_a_kind(self):
        self.count = 0
        self.option = 'Four of a Kind'
        self.winner_option()

    def full_house(self):
        self.count = 0
        self.option = 'Full House'
        self.winner_option()

    def flush(self):
        self.count = 0
        self.option = 'Flush'
        self.winner_option()

    def straight(self):
        self.count = 0
        self.option = 'Straight'
        self.winner_option()

    def three_of_a_kind(self):
        self.count = 0
        self.option = 'Three of a Kind'
        self.winner_option()

    def two_pair(self):
        self.count = 0
        self.option = 'Two Pair'
        self.winner_option()

    def one_pair(self):
        self.count = 0
        self.option = 'Pair'
        self.winner_option()

    def higher_card(self):
        self.count = 0
        self.option = 'High Card'
        self.winner_option()

    def show_winner(self):
        self.screen.label_p1bet.setText('')
        self.screen.label_p2bet.setText('')
        self.screen.label_p3bet.setText('')
        self.screen.label_p4bet.setText('')
        self.screen.label_p5bet.setText('')
        self.screen.label_p6bet.setText('')

        self.screen.p1_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[0][0]}.png"))
        self.screen.p1_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[0][1]}.png"))
        self.screen.p2_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[1][0]}.png"))
        self.screen.p2_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[1][1]}.png"))
        self.screen.p3_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[2][0]}.png"))
        self.screen.p3_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[2][1]}.png"))
        self.screen.p4_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[3][0]}.png"))
        self.screen.p4_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[3][1]}.png"))
        self.screen.p5_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[4][0]}.png"))
        self.screen.p5_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[4][1]}.png"))
        self.screen.p6_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[5][0]}.png"))
        self.screen.p6_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.playerstwocards[5][1]}.png"))
        self.screen.desk_card1.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.community_cards[0]}.png"))
        self.screen.desk_card2.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.community_cards[1]}.png"))
        self.screen.desk_card3.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.community_cards[2]}.png"))
        self.screen.desk_card4.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.community_cards[3]}.png"))
        self.screen.desk_card5.setPixmap(QtGui.QPixmap(
            f":/icon/{self.game.community_cards[4]}.png"))
        

        if 'Player1' in self.winner:
            self.screen.label_p1bet.setText('Winner')
        if 'Player2' in self.winner:
            self.screen.label_p2bet.setText('Winner')
        if 'Player3' in self.winner:
            self.screen.label_p3bet.setText('Winner')
        if 'Player4' in self.winner:
            self.screen.label_p4bet.setText('Winner')
        if 'Player5' in self.winner:
            self.screen.label_p5bet.setText('Winner')
        if 'Player6' in self.winner:
            self.screen.label_p6bet.setText('Winner')

        self.screen.label_playerturn.setText('Winner:{}\n{}\n{}'.format(self.winner[0:7],self.option,self.count))

    def getWinnerList(self):
        res = ""
        for i in range(0, len(self.game.winner_list), 2):
            res += str(int((i + 2) / 2)) + ". " + str(self.game.winner_list[i]) + " " + \
                str(self.game.winner_list[i+1]) + "\n"
        return res

    