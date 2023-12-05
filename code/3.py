import requests

url = 'https://adventofcode.com/2023/day/3/input'

cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)

    if response.status_code == 200:
        # part 1

        data = response.text
        lines = data.splitlines()
        matrix = [list(line) for line in lines]
        symbols = ['*', '$', '+', '#','-','/','@','=','&','%']
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,0],[-1,-1],[-1,1]]
        total = 0
        symbolAdjacent = False
        currentNum = 0
        numRows = len(matrix)
        numCols = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].isdigit() and currentNum == 0:
                    currentNum = matrix[i][j]
                    for direction in directions:
                        if 0 <= i + direction[0] < numRows and 0 <= j + direction[1] < numCols and matrix[i+direction[0]][j+direction[1]] in symbols:    
                            symbolAdjacent = True
                elif matrix[i][j].isdigit() and currentNum != 0:
                    currentNum = currentNum + matrix[i][j]
                    for direction in directions:
                        if 0 <= i + direction[0] < numRows and 0 <= j + direction[1] < numCols and matrix[i+direction[0]][j+direction[1]] in symbols:    
                            symbolAdjacent = True
                else:
                    if symbolAdjacent:
                        total += int(currentNum)
                    currentNum = 0
                    symbolAdjacent = False
        print(f"Part 1: {total}")

        # part 2

        data = response.text
        lines = data.splitlines()
        matrix = [list(line) for line in lines]
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        total = 0
        currentNum = 0
        numRows = len(matrix)
        numCols = len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '*':
                    newNum = True
                    numCount = 0

                    for direction in directions:
                        if direction[0] == 0 or direction == [1,-1] or not matrix[i+direction[0]][j+direction[1]].isdigit():
                            newNum = True

                        inbounds = 0 <= i+direction[0] < numRows and 0 <= j+direction[1] < numCols
                        if inbounds and matrix[i+direction[0]][j+direction[1]].isdigit() and newNum:
                            currentPos = [i+direction[0],j+direction[1]]
                            xOffset = -1
                            currentNum = matrix[currentPos[0]][currentPos[1]]
                            numCount += 1
                            newNum = False
                            inbounds = 0 <= j+direction[1] + xOffset < numCols

                            while inbounds and matrix[currentPos[0]][currentPos[1] + xOffset].isdigit():
                                currentNum = matrix[currentPos[0]][currentPos[1] + xOffset] + currentNum
                                xOffset -= 1
                                inbounds = 0 <= j+direction[1] + xOffset < numCols
                            xOffset = 1
                            inbounds = 0 <= j+direction[1] + xOffset < numCols

                            while inbounds and matrix[currentPos[0]][currentPos[1] + xOffset].isdigit():
                                currentNum = currentNum + matrix[currentPos[0]][currentPos[1] + xOffset]
                                xOffset += 1
                                inbounds = 0 <= j+direction[1] + xOffset < numCols

                            if(numCount == 1):
                                firstNum = currentNum
                
                    if numCount == 2:
                        total += int(firstNum) * int(currentNum)

        print(f"Part 2: {total}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()