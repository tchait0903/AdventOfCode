import requests
from math import lcm

url = 'https://adventofcode.com/2023/day/8/input'
cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)

    if response.status_code == 200:
        # part 1
        
        data = response.text
        total = 0
        lines = data.splitlines()
        directions = "".join(filter(str.isalpha, lines[:1]))
        locations = {}
        for line in lines[2:]:
            tokens = line.split(' ')
            locations[tokens[0]] = [tokens[2].replace('(','').replace(',',''), tokens[3].replace(')','')]

        currentLocation = 'AAA'
        while currentLocation != 'ZZZ':
            for direction in directions:
                if direction == 'L':
                    currentLocation = locations[currentLocation][0]
                elif direction == 'R':
                    currentLocation = locations[currentLocation][1]
                total += 1

        print(f"Part 1: {total}")

        # part 2
    
        data = response.text
        total = 0
        lines = data.splitlines()
        directions = "".join(filter(str.isalpha, lines[:1]))
        locations = {}
        for line in lines[2:]:
            tokens = line.split(' ')
            locations[tokens[0]] = [tokens[2].replace('(','').replace(',',''), tokens[3].replace(')','')]
        

        startingLocations = [key for key in locations if key.endswith("A")]
        stepDictionary = {}
        for location in startingLocations:
            steps = 0
            while location.endswith('Z') == False:
                for direction in directions:
                    if direction == 'L':
                            location = locations[location][0]
                    elif direction == 'R':
                            location = locations[location][1]
                    steps += 1
            stepDictionary[location] = steps
            total = lcm(*stepDictionary.values())

        print(f"Part 2: {total}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()