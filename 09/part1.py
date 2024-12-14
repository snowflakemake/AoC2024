class TrailHead:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.trails = [[(row, col)]]

heads = []
map = []
with open("09/small_input.txt", "r") as f:
    lines = f.readlines()
    for row, line in enumerate(lines):
        line = line.strip()
        map_row = []
        for col, letter in enumerate(line):
            if letter == '0':
                heads.append(TrailHead(row, col))
            map_row.append(int(letter))
        map.append(map_row)

for head in heads:
    print(head.row, head.col)
