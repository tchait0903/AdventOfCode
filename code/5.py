import requests

url = 'https://adventofcode.com/2023/day/5/input'
cookie = open('./cookie.txt', 'r').read()
session = requests.Session()
session.cookies.update({'session': cookie})

try:
    response = session.get(url)
    if response.status_code == 200:
        # part 1
    
        data = response.text
        lines = data.splitlines()
        seeds = [int(seed) for seed in lines[0].replace('seeds: ', '').split()]
        seedToSoilMap = {}
        S_to_FMap = {}
        F_to_WMap = {}
        W_to_LMap = {}
        L_to_TMap = {}
        T_to_HMap = {}
        H_to_LMap = {}

        def getMap(lines, sourceNums, mapName):
            for sourceNum in sourceNums:
                for line in lines:
                    tokens = line.split()
                    dest = int(tokens[0])
                    source = int(tokens[1])
                    rangeNum = int(tokens[2])
                    if source <= sourceNum < source + rangeNum:
                        mapName[sourceNum] = dest + (sourceNum - source)
                        break
                    else:
                        mapName[sourceNum] = sourceNum
            return mapName


        seedToSoilMap = getMap(lines[3:29], seeds, seedToSoilMap)
        S_to_FMap = getMap(lines[31:50], seedToSoilMap.values(), S_to_FMap)
        F_to_WMap = getMap(lines[52:96], S_to_FMap.values(), F_to_WMap)
        W_to_LMap = getMap(lines[98:119], F_to_WMap.values(), W_to_LMap)
        L_to_TMap = getMap(lines[121:152], W_to_LMap.values(), L_to_TMap)
        T_to_HMap = getMap(lines[154:203], L_to_TMap.values(), T_to_HMap)
        H_to_LMap = getMap(lines[205:], T_to_HMap.values(), H_to_LMap)

        print(f"Part 1: {min(H_to_LMap.values())}")

        # part 2
        data = response.text

        data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
        lines = data.splitlines()
        seeds = [int(seed) for seed in lines[0].replace('seeds: ', '').split()]
        #print(seeds)
        seedToSoilMap = {}
        S_to_FMap = {}
        F_to_WMap = {}
        W_to_LMap = {}
        L_to_TMap = {}
        T_to_HMap = {}
        H_to_LMap = {}

        def getMap(lines, sourceNums, mapName):
            #print(mapName)
            for sourceNum in sourceNums:
                #print(f"sourceNum: {sourceNum}")
                for line in lines:
                    #print(line)
                    tokens = line.split()
                    dest = int(tokens[0])
                    source = int(tokens[1])
                    rangeNum = int(tokens[2])
                    #print(f"{source} <= {sourceNum} < {source + rangeNum}")
                    if source <= sourceNum < source + rangeNum:
                        mapName[sourceNum] = dest + (sourceNum - source)
                        break
                    else:
                        mapName[sourceNum] = sourceNum
            return mapName

        # input line values
        # seedToSoilMap = getMap(lines[3:29], seeds, seedToSoilMap)
        # S_to_FMap = getMap(lines[31:50], seedToSoilMap.values(), S_to_FMap)
        # F_to_WMap = getMap(lines[52:96], S_to_FMap.values(), F_to_WMap)
        # W_to_LMap = getMap(lines[98:119], F_to_WMap.values(), W_to_LMap)
        # L_to_TMap = getMap(lines[121:152], W_to_LMap.values(), L_to_TMap)
        # T_to_HMap = getMap(lines[154:203], L_to_TMap.values(), T_to_HMap)
        # H_to_LMap = getMap(lines[205:], T_to_HMap.values(), H_to_LMap)

        seedToSoilMap = getMap(lines[3:5], seeds, seedToSoilMap)
        S_to_FMap = getMap(lines[31:50], seedToSoilMap.values(), S_to_FMap)
        F_to_WMap = getMap(lines[52:96], S_to_FMap.values(), F_to_WMap)
        W_to_LMap = getMap(lines[98:119], F_to_WMap.values(), W_to_LMap)
        L_to_TMap = getMap(lines[121:152], W_to_LMap.values(), L_to_TMap)
        T_to_HMap = getMap(lines[154:203], L_to_TMap.values(), T_to_HMap)
        H_to_LMap = getMap(lines[205:], T_to_HMap.values(), H_to_LMap)

        print(f"Part 1: {min(H_to_LMap.values())}")

    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    session.close()