players = {
    "P1": ["10J", "10H"],
    "P2": ["QD", "KD"],
    "P3": ["QC", "5H"],
    "P4": ["3D", "3S"],
    "P5": ["6D", "8H"],
    "P6": ["7H", "10S"],
}
community_cards = ["4H", "3H", "3J", "10C", "10D"]


def find_four_of_a_kind_winner(players, community_cards):
    max_rank = -1
    winner = None
    for player, hand in players.items():
        all_cards = hand + community_cards
        rank_counts = {}
        for card in all_cards:
            rank = card[:-1]
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        for rank, count in rank_counts.items():
            if count == 4 and int(rank) > max_rank:
                max_rank = int(rank)
                winner = player
    return winner


winner = find_four_of_a_kind_winner(players, community_cards)
print("Winner:", winner)
