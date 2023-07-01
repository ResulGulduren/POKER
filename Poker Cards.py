import random


def create_deck():
    deck = []
    suits = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs Spades
    ranks = [
        "A",
        "K",
        "Q",
        "J",
        "10",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
    ]  # Ace, King, Queen, Jack

    for suit in suits:
        for rank in ranks:
            hand = rank + suit
            deck.append(hand)
    return deck


def distrubition(deck, number_of_players):
    players_two_cards = {}
    random.shuffle(deck)
    for _ in range(number_of_players):
        player_name = "P" + str(_ + 1)
        players_two_cards[player_name] = []

        for _ in range(2):
            players_two_cards[player_name].append(deck[_])
            deck.pop(_)
    return players_two_cards


def check_winner():
    if check_royal_flush():
        return
    if check_straight_flush():
        return
    if check_four_of_a_kind():
        return
    if check_full_house():
        return
    if check_flush():
        return
    if check_straight():
        return
    if check_three_of_a_kind():
        return
    if check_two_pair():
        return
    if check_pair():
        return
    if check_high_card():
        return


def check_royal_flush():
    pass


def check_straight_flush():
    pass


def check_four_of_a_kind():
    pass


def check_full_house():
    pass


def check_flush():
    pass


def check_straight():
    pass


def check_three_of_a_kind():
    pass


def check_two_pair():
    pass


def check_pair():
    pass


def check_high_card():
    pass


# Main Program
number_of_players = 6
community_cards_count = 5
winner = False
attempt = 0

while winner == False:
    deck = create_deck()
    players_two_cards = distrubition(deck, number_of_players)
    community_cards = random.sample(deck, community_cards_count)
    # deck = [card for card in deck if card not in community_cards]
    # Burasi aslinda gereksiz artik kalan kartlarla bir isimiz yok.
    # Fakat eger parca parca kartlar dagitilsa (3+1+1) bunu o zaman yapmak gerekiyor.
    attempt += 1
    players_all_cards = {}
    for players, cards in players_two_cards.items():
        all_cards = []
        all_cards.extend(cards)
        all_cards.extend(community_cards)
        players_all_cards[players] = all_cards
    # for i,j in p_cards.items():
    #         a=[]
    #         a.extend(j)
    #         a.extend(c_cards)
    #         player_control_dic[i]=a
    print(deck)
    print(len(deck))
    print(players_two_cards)
    print(players_all_cards)
    print(community_cards)
    break
    check_winner()
