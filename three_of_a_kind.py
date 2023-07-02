p_cards = {
    'P1': ['AS', 'AD'],
    'P2': ['QD', 'KD'],
    'P3': ['QC', 'QS'],
    'P4': ['3D', '3S'],
    'P5': ['6D', '8H'],
    'P6': ['5D', '10S']
}

c_cards = ['4H', 'AH', 'KH', 'QH', '9H']


def get_card_rank(value):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return ranks.get(value, 0)

def three_of_a_kind(p_cards, c_cards):
    player_control_dic = {}
    for player, cards in p_cards.items():
        a = []
        a.extend(cards)
        a.extend(c_cards)
        player_control_dic[player] = a

    winners = []
    highest_rank = 0
    for player, cards in player_control_dic.items():
        card_values = [card[:-1] for card in cards]
        value_counts = {value: card_values.count(value) for value in card_values}
        if 3 in value_counts.values():
            rank = get_card_rank(max(value_counts, key=value_counts.get))
            if rank > highest_rank:
                highest_rank = rank
                winners = [player]
            elif rank == highest_rank:
                winners.append(player)
    return winners

print(three_of_a_kind(p_cards, c_cards))