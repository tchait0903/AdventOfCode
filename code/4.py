import requests

url = 'https://adventofcode.com/2023/day/4/input'
cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)
    if response.status_code == 200:
        # part 1
    
        data = response.text
        lines = data.splitlines()
        total = 0 
        for line in lines:
            oneMatch = False
            cardSum = 0
            tokens = line.split()
            winNums = tokens[2:12]
            myNums = tokens[13:]
            for num in myNums:
                if num in winNums:
                    if not oneMatch:
                        cardSum += 1
                        oneMatch = True
                    else:
                        cardSum *= 2
            total += cardSum
        print(f"Part 1: {total}")

        # part 2

        data = response.text
        lines = data.splitlines()
        total = 0
        dict = {i:1 for i in range(1,len(lines)+1)}
        for line in lines:
            tokens = line.split()
            cardId = int(tokens[1].replace(':',''))
            winNums = set(tokens[2:12])
            myNums = set(tokens[13:])
            for i in range(dict[cardId]):
                cardSum = sum(1 for num in myNums if num in winNums)
                for j in range(cardId+1,cardSum + cardId+1):
                    if j in dict:
                        dict[j] += 1
        print(f"Part 2: {sum(dict.values())}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()