players={'P1': ['2D', '8D'],
         'P2': ['8C', 'KS'],
         'P3': ['AC', 'QH'],
         'P4': ['3D', '3S'],
         'P5': ['KD', '2H'],
         'P6': ['10D', '10S']}
community_cards=['10H', '7D', '8S', '1S', '8D']
def find_two_pair_winner(players, community_cards):
    max_rank = -1
    winners = []
    for player, hand in players.items():
        all_cards = hand + community_cards
        rank_counts = {}
        for card in all_cards:
            rank = card[:-1]
            rank_value = rank_to_value(rank)
            rank_counts[rank_value] = rank_counts.get(rank_value, 0) + 1
        pair_ranks = []
        for rank, count in rank_counts.items():
            if count == 2:
                pair_ranks.append(rank)
        if len(pair_ranks) >= 2:
            max_pair_rank = max(pair_ranks)
            if max_pair_rank > max_rank:
                max_rank = max_pair_rank
                winners = [player]
            elif max_pair_rank == max_rank:
                winners.append(player)
    return winners
def rank_to_value(rank):
    rank_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return rank_values.get(rank, 0)
winners = find_two_pair_winner(players, community_cards)
print("Winners:", winners)
