players={'P1': ['2D', '8D'], 
         'P2': ['6C', '3S'], 
         'P3': ['QC', '2H'], 
         'P4': ['3D', '3S'], 
         'P5': ['2D', '2H'], 
         'P6': ['QD', '10S']}
community_cards=['4H', '8D', '8S', '1S', '9D']




def rank_to_value(rank):
    rank_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return rank_values.get(rank, 0)

def find_high_card_winner(players, community_cards):
    max_rank = -1
    winners = []

    for player, hand in players.items():
        all_cards = hand + community_cards
        rank_values = [rank_to_value(card[:-1]) for card in all_cards]
        max_hand_rank = max(rank_values)

        if max_hand_rank > max_rank:
            max_rank = max_hand_rank
            winners = [player]
        elif max_hand_rank == max_rank:
            winners.append(player)

    return winners

winners = find_high_card_winner(players, community_cards)
print("Winners:", winners)
