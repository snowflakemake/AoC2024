class TrailHead:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.trails = [[(row, col)]]

heads = []
map = []
with open("10/input.txt", "r") as f:
    lines = f.readlines()
    for row, line in enumerate(lines):
        line = line.strip()
        map_row = []
        for col, letter in enumerate(line):
            if letter == '0':
                heads.append(TrailHead(row, col))
            map_row.append(int(letter))
        map.append(map_row)

def checkSurroundings(val, row, col, map):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    availableRoutes = []
    for dx, dy in directions:
        new_row = row + dx
        new_col = col + dy
        if 0 <= new_row < len(map) and 0 <= new_col < len(map[0]):
            if map[new_row][new_col] == val + 1:
                availableRoutes.append((new_row, new_col))
    return availableRoutes

for head in heads:
    for trail in head.trails:
        row, col = trail[-1]  # Correctly unpack the last tuple
        while True:
            availableRoutes = checkSurroundings(map[row][col], row, col, map)
            if len(availableRoutes) == 0: 
                break
            if len(availableRoutes) > 1:
                for i in range(1, len(availableRoutes)):
                    trailCopy = trail.copy()  # Ensure you copy the trail correctly
                    trailCopy.append(availableRoutes[i])
                    head.trails.append(trailCopy)
            new_row, new_col = availableRoutes[0]
            trail.append((new_row, new_col))
            row, col = new_row, new_col
          
scoreSum = 0            
for head in heads:
    visitedNines = []
    score = 0
    print(f"Head at ({head.row}, {head.col}):")
    for trail in head.trails:
        if len(trail) == 10 and trail[-1] not in visitedNines:
            print(trail)
            visitedNines.append(trail[-1])
            score += 1
    print(f"Score: {score}")
    scoreSum += score
    
print(f"Total: {scoreSum}")

# Part 2
scoreSum = 0            
for head in heads:
    score = 0
    print(f"Head at ({head.row}, {head.col}):")
    for trail in head.trails:
        if len(trail) == 10:
            print(trail)
            score += 1
    print(f"Score: {score}")
    scoreSum += score
    
print(f"Total: {scoreSum}")