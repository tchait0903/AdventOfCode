import requests

url = 'https://adventofcode.com/2023/day/2/input'

cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)

    if response.status_code == 200:
        # part 1

        redThreshold = 12
        greenThreshold = 13
        blueThreshold = 14
        games = response.text.splitlines()
        total = 0
        for game in games:
            greenMax, blueMax, redMax = 0, 0, 0
            tokens = game.split()
            id = int(tokens[1].replace(':', ''))
            for i in range(0, len(tokens) - 1, 2):
                current_token = tokens[i]
                next_token = tokens[i + 1]

                if current_token.isdigit():
                    num = int(current_token)

                    if next_token.startswith('green'):
                        if num > greenMax:
                            greenMax = num
                    elif next_token.startswith('blue'):
                        if num > blueMax:
                            blueMax = num
                    elif next_token.startswith('red'):
                        if num > redMax:
                            redMax = num
            if greenMax <= greenThreshold and blueMax <= blueThreshold and redMax <= redThreshold:
                total += id
        print(f"Part 1: {total}")
        
        # part 2

        total = 0
        for game in games:
            greenMax, blueMax, redMax = 0, 0, 0
            tokens = game.split()
            for i in range(0, len(tokens) - 1, 2):
                current_token = tokens[i]
                next_token = tokens[i + 1]

                if current_token.isdigit():
                    num = int(current_token)

                    if next_token.startswith('green'):
                        if num > greenMax:
                            greenMax = num
                    elif next_token.startswith('blue'):
                        if num > blueMax:
                            blueMax = num
                    elif next_token.startswith('red'):
                        if num > redMax:
                            redMax = num
            total += greenMax * blueMax * redMax
        print(f"Part 2: {total}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()