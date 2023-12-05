import requests

url = 'https://adventofcode.com/2023/day/1/input'

cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)

    if response.status_code == 200:
        # part 1
    
        data = response.text
        total = 0
        for line in data.splitlines():
            line = ''.join(char for char in line if not char.isalpha())
            total += int(line[0]+line[-1])

        print(f"Part 1: {total}")

        # part 2

        total = 0
        num_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
        for line in data.splitlines():
            for word, number in num_dict.items():
                if word in line:
                    line = line.replace(word, word[0] + number + word[-1])
            line = ''.join(char for char in line if not char.isalpha())
            total += int(line[0] + line[-1])

        print(f"Part 2: {total}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()