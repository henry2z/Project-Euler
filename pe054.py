f = open('pe054_poker.txt')
games = f.read().split('\n')

def card_type(cards):
    values = []
    types = []
    is_flush = False
    is_straight = False
    cards = cards.split()
    for i in range(len(cards)):
        flag = True
        value = int(cards[i][:-1])
        for j in range(len(values)):
            if value == values[j][1]:
                values[j][0] += 1
                flag = False
        if flag:
            values.append([1, value])
        types.append(cards[i][-1])
    values = sorted(values, reverse=True)
    if len(set(types)) == 1:
        is_flush = True
    if values[0][1] - values[-1][1] == 4:
        is_straight = True
    elif (values[-1][1] - 13) - values[0][1] == 4:
        is_straight = True
        values[-1][1] = 1
        values = sorted(values, reverse=True)
    
    if len(values) == 5 and (not is_straight) and (not is_flush):
        return 0, max([l[1] for l in values])
    elif values[0][0] == 2 and not values[1][0] == 2:
        return 1, values[0][1], max(values[1][1], values[2][1])
    elif values[0][0] == 2 and values[1][0] == 2:
        return 2, values[0][1]
    elif values[0][0] == 3 and values[1][0] == 1:
        return 3, values[0][1], values[1][1]
    elif is_straight and not is_flush:
        return 4, values[0][1]
    elif is_flush and not is_straight:
        return 5, values[0][1]
    elif values[0][0] == 3 and values[1][0] == 2:
        return 6, values[0][1], values[1][1]
    elif values[0][0] == 4:
        return 7, values[0][1]
    elif is_straight and is_flush:
        return 8, values[0][1]


def winner(cards1, cards2):
    player1 = card_type(cards1)
    player2 = card_type(cards2)
    if player1[0] > player2[0]:
        return 1
    elif player1[0] < player2[0]:
        return 2
    else:
        if player1[1] > player2[1]:
            return 1
        elif player1[1] < player2[1]:
            return 2
        else:
            if player1[2] > player2[2]:
                return 1
            else:
                return 2


player1_wins = 0
for game in games:
    cards1 = game[:14]
    cards2 = game[15:]
    cards1 = cards1.replace('T', '10')
    cards1 = cards1.replace('J', '11')
    cards1 = cards1.replace('Q', '12')
    cards1 = cards1.replace('K', '13')
    cards1 = cards1.replace('A', '14')
    cards2 = cards2.replace('T', '10')
    cards2 = cards2.replace('J', '11')
    cards2 = cards2.replace('Q', '12')
    cards2 = cards2.replace('K', '13')
    cards2 = cards2.replace('A', '14')
    if winner(cards1, cards2) == 1:
        player1_wins += 1
print(player1_wins)

# for game in games[-10:]:
#     cards1 = game[:14]
#     cards2 = game[15:]
#     cards1 = cards1.replace('T', '10')
#     cards1 = cards1.replace('J', '11')
#     cards1 = cards1.replace('Q', '12')
#     cards1 = cards1.replace('K', '13')
#     cards1 = cards1.replace('A', '14')
#     cards2 = cards2.replace('T', '10')
#     cards2 = cards2.replace('J', '11')
#     cards2 = cards2.replace('Q', '12')
#     cards2 = cards2.replace('K', '13')
#     cards2 = cards2.replace('A', '14')
#     print(cards1 + ' and ' + cards2, winner(cards1, cards2))

# print(card_type('13H 11S 4H 5D 9D'))
# print(card_type('10C 10D 12C 11D 10S'))