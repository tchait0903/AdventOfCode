import requests

url = 'https://adventofcode.com/2023/day/9/input'
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
            matrix = [[int(num) for num in line.split(' ')]]
            allNumsAreNotZero = True
            row = 0

            while allNumsAreNotZero:
                newRow = []
                for i in range(1,len(matrix[row])):
                    num = matrix[row][i]
                    lastNum = matrix[row][i-1]
                    newRow.append(num - lastNum)

                matrix.append(newRow)
                row += 1
                if all(num == 0 for num in newRow):
                    allNumsAreNotZero = False

            for i in range(len(matrix)-2, -1, -1):
                    matrix[i].append(matrix[i][-1] + matrix[i+1][-1])

            total += matrix[0][-1]

        print(f"Part 1: {total}")

        # part 2
    
        data = response.text
        total = 0
        for line in data.splitlines():
            matrix = [[int(num) for num in line.split(' ')]]
            allNumsAreNotZero = True
            row = 0

            while allNumsAreNotZero:
                newRow = []
                for i in range(1,len(matrix[row])):
                    num = matrix[row][i]
                    lastNum = matrix[row][i-1]
                    newRow.append(num - lastNum)

                matrix.append(newRow)
                row += 1
                if all(num == 0 for num in newRow):
                    allNumsAreNotZero = False

            for i in range(len(matrix)-2, -1, -1):
                    matrix[i].insert(0, matrix[i][0] - matrix[i+1][0])

            total += matrix[0][0]

        print(f"Part 2: {total}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()