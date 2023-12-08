import requests

url = 'https://adventofcode.com/2023/day/7/input'
cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)

    if response.status_code == 200:
        # part 1
        
        data = response.text
       
        cardStrengthOrder = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        handStrengthOrder = ['High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Full House', 'Four of a Kind', 'Five of a Kind']
        total = 0
        hands = {}

        def checkForHandType(hand):
            counts = {}
            for card in hand:
                counts[card] = hand.count(card)
            if(max(counts.values()) == 5):
                return 'Five of a Kind'
            elif(max(counts.values()) == 4):
                return 'Four of a Kind'
            elif(max(counts.values()) == 3):
                if(len(counts) == 2):
                    return 'Full House'
                else:
                    return 'Three of a Kind'
            elif(max(counts.values()) == 2):
                if(len(counts) == 3):
                    return 'Two Pair'
                else:
                    return 'One Pair'
            else:
                return 'High Card'

        for line in data.splitlines():
            hands[line.split(' ')[0]] = [line.split(' ')[1]]
            hands[line.split(' ')[0]].append(checkForHandType(line.split(' ')[0]))
       
        sortedHands = sorted(hands.keys(), key=lambda x: (handStrengthOrder.index(hands[x][1]), [cardStrengthOrder.index(ch) for ch in x]))
        for hand in sortedHands:
            total += int(hands[hand][0]) * (sortedHands.index(hand)+1)


        print(f"Part 1: {total}")


        # part 2

        data = response.text
        cardStrengthOrder = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        handStrengthOrder = ['High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Full House', 'Four of a Kind', 'Five of a Kind']
        total = 0
        cards = {}
        hands = {}

        def checkForHandType(hand):
            counts = {}
            for card in hand:
                counts[card] = hand.count(card)
            countsWithoutJ = {k: v for k, v in counts.items() if k != 'J'}
            maxWithJokers = max(countsWithoutJ.values(), default=0) + hand.count('J')

            if(maxWithJokers == 5):
                return 'Five of a Kind'
            elif(maxWithJokers == 4):
                return 'Four of a Kind'
            elif(maxWithJokers == 3):
                if(len(counts) == 2 or (len(counts) == 3 and hand.count('J') > 0)):
                    return 'Full House'
                else:
                    return 'Three of a Kind'
            elif(maxWithJokers == 2):
                if(len(counts) == 3 or (len(counts) == 4 and hand.count('J') > 0)):
                    return 'Two Pair'
                else:
                    return 'One Pair'
            else:
                return 'High Card'

        for line in data.splitlines():
            hands[line.split(' ')[0]] = [line.split(' ')[1]]
            hands[line.split(' ')[0]].append(checkForHandType(line.split(' ')[0]))
       
        sortedHands = sorted(hands.keys(), key=lambda x: (handStrengthOrder.index(hands[x][1]), [cardStrengthOrder.index(ch) for ch in x]))
        for hand in sortedHands:
            total += int(hands[hand][0]) * (sortedHands.index(hand)+1)

        print(f"Part 2: {total}")


    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()