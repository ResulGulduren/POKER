# import itertools
import random, sqlite3


class PokerGame:
    def __init__(self):
        self.deck_of_cards = self.create_card_deck()
        self.community_cards = []
        self.playerstwocards = []
        self.rank_names = [
            "High Card",
            "Pair",
            "Two Pair",
            "Three of a Kind",
            "Straight",
            "Flush",
            "Full House",
            "Four of a Kind",
            "Straight Flush",
            "Royal Flush",
        ]
        self.hand_evaluation = []
        
        for _ in range(6):
            player_cards = self.deal_cards(2)
            self.playerstwocards.append(player_cards)

        self.community_cards = self.deal_cards(5)

        for index, player in enumerate(self.playerstwocards):
            players_hand = player + self.community_cards
            hand = self.hand_rank(players_hand)
            self.hand_evaluation.append(hand)
       
        evaluation = self.find_winner(self.hand_evaluation)
        
        
        

        # Veritabanı bağlantısı
        connection = sqlite3.connect("poker_statistic.db")
        cursor = connection.cursor()

        # Oyun sonucunu kaydetme
        winner_index = evaluation.index(max(evaluation))
        winner_hand = self.playerstwocards[winner_index]
        total_games = 1  # Her oyun sonucunda toplam oyun sayısını 1 artırıyoruz

        # Oyuncu elinin veritabanında olup olmadığını kontrol etme
        cursor.execute("SELECT * FROM winners WHERE hand = ?", (str(winner_hand),))
        existing_hand = cursor.fetchone()

        if existing_hand is not None:
            # El zaten veritabanında kayıtlıysa sadece total_games ve wined_games değerlerini güncelle
            total_games += existing_hand[1]
            win_games = existing_hand[2] + 1
            win_rate = win_games / total_games  # Kazanma oranını hesapla
            cursor.execute(
                "UPDATE winners SET total_games = ?, wined_games = ?, rate = ? WHERE hand = ?",
                (total_games, win_games, win_rate, str(winner_hand)),
            )
        else:
            # El veritabanında kayıtlı değilse yeni bir kayıt oluştur
            cursor.execute(
                "INSERT INTO winners (hand, total_games, wined_games, rate) VALUES (?, ?, ?, ?)",
                (str(winner_hand), total_games, 1, 1.0),  # İlk kazanan el için kazanma oranı 1 olarak varsayıldı
            )

        # Diğer oyuncuların total_games değerini 1 artırma
        for i, player_hand in enumerate(self.playerstwocards):
            if i != winner_index:
                cursor.execute(
                    "SELECT * FROM winners WHERE hand = ?", (str(player_hand),)
                )
                existing_hand = cursor.fetchone()
                if existing_hand is not None:
                    total_games = existing_hand[1] + 1
                    win_rate = existing_hand[3]  # Kazanma oranını aynen kullan
                    cursor.execute(
                        "UPDATE winners SET total_games = ?, rate = ? WHERE hand = ?",
                        (total_games, win_rate, str(player_hand)),
                    )
                else:
                    cursor.execute(
                        "INSERT INTO winners (hand, total_games, wined_games, rate) VALUES (?, ?, ?, ?)",
                        (str(player_hand), 1, 0, 0.0),  # Kazanma oranı 0 olarak varsayıldı
                    )

        # Veritabanını kaydetme ve bağlantıyı kapatma
        connection.commit()
        connection.close()

        

    def create_card_deck(self):
        card_deck = []
        for suit in ["H", "S", "D", "C"]:  # Hearts, Diamonds, Clubs, Spades
            for value in range(2, 11):
                card_deck.append((str(value) + suit))
            card_deck.append(("J" + suit))  # Ace, King, Queen, Jack
            card_deck.append(("Q" + suit))
            card_deck.append(("K" + suit))
            card_deck.append(("A" + suit))
        return card_deck

    def deal_cards(self, count):
        dealt_cards = []
        for _ in range(count):
            card = random.choice(self.deck_of_cards)
            self.deck_of_cards.remove(card)
            dealt_cards.append(card)
        return dealt_cards

    def check_royal_flush(self, hand):
        hand_check = []
        for card in hand:
            if (
                self.value(card) == 14
                or self.value(card) == 13
                or self.value(card) == 12
                or self.value(card) == 11
                or self.value(card) == 10
            ):
                hand_check.append(card)
        total = self.define_suit(hand_check)
        if max(total.values()) == 5:
            return True
        return False

    def define_suit(self, hand):
        suits_hand = {"C": 0, "D": 0, "H": 0, "S": 0}
        for card in hand:
            suits_hand[card[-1]] += 1
        return suits_hand

    def check_flush(self, hand):
        define = self.define_suit(hand)
        if define["C"] >= 5 or define["D"] >= 5 or define["H"] >= 5 or define["S"] >= 5:
            return True
        else:
            return False

    def value(self, card):
        if card[0] == "A":
            return 14
        elif card[0] == "K":
            return 13
        elif card[0] == "Q":
            return 12
        elif card[0] == "J":
            return 11
        else:
            return int(card[:-1])

    def hand_dist(self, hand):
        dist = {i: 0 for i in range(1, 15)}
        for card in hand:
            dist[self.value(card)] += 1
        dist[1] = dist[14]
        return dist

    def check_straight(self, hand):
        dist = self.hand_dist(hand)
        # {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1}
        for value in range(1, 11):
            if all([dist[value + k] >= 1 for k in range(5)]):
                return True
        return False
    
    def check_straight_flush(self, hand):
        define = self.define_suit(hand)
        max_suit = max(define, key=define.get)
        control_list = [card for card in hand if card[-1] == max_suit]
        if len(control_list) >= 5:
            result = self.check_straight(control_list)
            return result
        else:
            return False
        
    def card_count(self, hand, num, but=None):
        dist = self.hand_dist(hand)
        for value in range(2, 15):
            if value == but:
                continue
            if dist[value] == num:
                return value
        return None

    def check_high_card(self, hand):
        return max(self.value(card) for card in hand)

    
    def hand_rank(self, hand):
        if self.check_royal_flush(hand):
            return 9
        if self.check_straight_flush(hand):
            return 8
        if self.card_count(hand, 4) is not None:
            return 7
        if (
            self.card_count(hand, 3) is not None
            and self.card_count(hand, 2) is not None
        ) or self.card_count(hand, 3, self.card_count(hand, 3)) is not None:
            return 6
        if self.check_flush(hand):
            return 5
        if self.check_straight(hand):
            return 4
        if self.card_count(hand, 3) is not None:
            return 3
        pair1 = self.card_count(hand, 2)
        if pair1 is not None:
            if self.card_count(hand, 2, but=pair1) is not None:
                return 2
            return 1
        return 0

    def find_winner(self, list):
        
        self.number = max(list)
        winnerindex = list.index(self.number)
        winner = "Player{} Hand: {} Ranking: {}".format(
            winnerindex + 1, self.playerstwocards[winnerindex], self.rank_names[self.number]
        )
        return winner
        # one_winner = list.count(number)
        # if one_winner == 1:
        #     winnerindex = list.index(number)
        #     winner = "Player{} Hand:{} Ranking:{}" .format(winnerindex+1, self.playerstwocards[winnerindex], self.rank_names[number])
        #     return winner
        # else:
        #     self.start_game(6)

    def start_game(self, num_players):
        pass
        
    def restart_game(self):
        self.community_cards = []
        self.playerstwocards = []
        self.create_card_deck()
        for _ in range(6):
            player_cards = self.deal_cards(2)
            self.playerstwocards.append(player_cards)
        self.community_cards = self.deal_cards(5)
       
PokerGame()

# if __name__ == "__main__":
#      poker_game = PokerGame()
#      poker_game.start_game(6)

# ...

