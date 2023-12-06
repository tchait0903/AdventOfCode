import requests

url = 'https://adventofcode.com/2023/day/6/input'
cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)

    if response.status_code == 200:
        # part 1
        
        data = response.text
        times = [int(time) for time in data.splitlines()[0].split()[1:]]
        distances = [int(distances) for distances in data.splitlines()[1].split()[1:]]
        total = 1
        for time, distance in zip(times, distances):
            count = 0
            for i in range(time+1):
                if i * (time - i) > distance:
                    count += 1
            total *= count
        
        print(f"Part 1: {total}")

        # part 2
    
        data = response.text
        time = int(''.join(data.splitlines()[0].split()[1:]))
        distance = int(''.join(data.splitlines()[1].split()[1:]))
        total = 1
        count = 0
        for i in range(time+1):
            if i * (time - i) > distance:
                count += 1
        total *= count

        print(f"Part 2: {total}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()