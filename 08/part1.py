import math

symbols = []
antennas = []
map = []
unique_locations = 0

with open("08/input.txt", "r") as f:
    lines = f.readlines()
    for row_index, row in enumerate(lines):
        row = row.strip()
        for col_index, symbol in enumerate(row):
            if symbol != '.':
                antennas.append([symbol, (row_index, col_index)])
        map.append(list(row))
        
symbols = set([item[0] for item in antennas])
for antenna in antennas:
    print(f"{antenna[0]}: {antenna[1]}")

for symbol in symbols:
    symbol_antennas = [antenna for antenna in antennas if antenna[0] == symbol]
    symbol_antenna_count = len(symbol_antennas)
    number_of_pairs = int((symbol_antenna_count * (symbol_antenna_count - 1)) / 2)
    
    print(f"Symbol: {symbol}")
    print(f"Number of pairs: {number_of_pairs}")

    for i in range(symbol_antenna_count):
        for j in range(i + 1, symbol_antenna_count):
            x1 = (symbol_antennas[i][1][1])
            x2 = (symbol_antennas[j][1][1])
            y1 = (symbol_antennas[i][1][0])
            y2 = (symbol_antennas[j][1][0])

            delta_x = x2-x1
            delta_y = y2-y1
            step = 0

            while True:
                x3 = x2+(delta_x*step)
                y3 = y2+(delta_y*step)
                print(y3, x3)
                if y3 < 0 or x3 < 0 or y3 >= len(map) or x3 >= len(map[0]):
                    break
                map[y3][x3] = '¤'
                step += 1

            step = 0
            while True:
                x4 = x1-(delta_x*step)
                y4 = y1-(delta_y*step)
                print(y4, x4)
                if y4 < 0 or x4 < 0 or y4 >= len(map) or x4 >= len(map[0]):
                    break
                map[y4][x4] = '¤'
                step += 1


for row in map:
    print(row)
    for col in row:
        if col == "¤":
            unique_locations += 1

print(f"Unique locations: {unique_locations}")