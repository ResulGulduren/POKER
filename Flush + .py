players = {
    "P1": ["10J", "8J"],
    "P2": ["QD", "KD"],
    "P3": ["QJ", "5J"],
    "P4": ["3D", "3S"],
    "P5": ["KJ", "4J"],
    "P6": ["5D", "10S"],
}
community_cards = ["4H", "2J", "3J", "1J", "10D"]


def find_flush_winner(players, community_cards):
    max_rank = -1
    winners = []
    for player, hand in players.items():
        all_cards = hand + community_cards
        suit_counts = {}
        for card in all_cards:
            suit = card[-1:]
            suit_counts[suit] = suit_counts.get(suit, 0) + 1
        for suit, count in suit_counts.items():
            if count >= 5:
                flush_cards = [card for card in all_cards if card[-1:] == suit]
                flush_cards.sort(key=lambda x: rank_to_value(x[:-1]), reverse=True)
                rank = rank_to_value(flush_cards[0][:-1])
                if rank > max_rank:
                    max_rank = rank
                    winners = [player]
                elif rank == max_rank:
                    winners.append(player)
    return winners


def rank_to_value(rank):
    rank_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    return rank_values.get(rank, 0)


winners = find_flush_winner(players, community_cards)
print("Winners:", winners)
