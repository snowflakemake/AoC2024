'''
ATTENTION!
Failed to completed this and wanted to continue with a new problem...
The solution below works on the smaller test but gives a too low answer
on the real input.

Well well..
'''
map = []
passed_map = []
pos = []
GUARD_ROTATIONS = ['^','>','v','<']
current_guard_rotation = 0
PASSED_CELL = "X"
OBSTACLE = "#"
DIRECTION_VECTORS = [[-1, 0],[0, 1],[1, 0],[0, -1]]
direction_vector = []
distinct_positions = 0
placed_obstacles = []
coordinate_directions = {}

with open("06/input.txt", "r") as f:
    lines = f.readlines()
    for row, line in enumerate(lines):
        passed_map.append(['.' for i in range(len(line))])
        line_list = []
        for col, letter in enumerate(line.strip()):
            line_list.append(letter)
            if letter in GUARD_ROTATIONS: 
                pos = [row, col]
                for i in range(len(GUARD_ROTATIONS)):
                    if GUARD_ROTATIONS[i] == letter:
                        current_guard_rotation = i
                try:
                    coordinate_directions[row,col].append(current_guard_rotation)
                except:
                    coordinate_directions[row,col] = [current_guard_rotation]
                passed_map[row][col] = PASSED_CELL
                distinct_positions += 1
                direction_vector = DIRECTION_VECTORS[current_guard_rotation]
        map.append(line_list)

def movement_allowed(map: list, pos: list, direction_vector: list):
    next_pos = [pos[0] + direction_vector[0], pos[1] + direction_vector[1]]
    if next_pos[0] >= len(map) or next_pos[1] >= len(map[0]) or next_pos[0] < 0 or next_pos[1] < 0:
        return None
    return not map[next_pos[0]][next_pos[1]] == OBSTACLE

def rotate_guard(direction_vector: list):
    global current_guard_rotation
    if current_guard_rotation < 3:
        current_guard_rotation += 1
    else: current_guard_rotation = 0
    return DIRECTION_VECTORS[current_guard_rotation]

from time import sleep
def part2(map, pos, direction_vector):
    global coordinate_directions
    global placed_obstacles
    next_guard_rotation = current_guard_rotation + 1
    if next_guard_rotation == 4: next_guard_rotation = 0
    next_next_guard_rotation = next_guard_rotation + 1
    if next_next_guard_rotation == 4: next_next_guard_rotation = 0
    step = 0
    while True:
        step += 1
        checking_row = DIRECTION_VECTORS[next_guard_rotation][0] * step + pos[0]
        checking_col = DIRECTION_VECTORS[next_guard_rotation][1] * step + pos[1]
        try:
            if map[checking_row][checking_col] == OBSTACLE: return False
            if checking_row== -1 or checking_col == -1: raise IndexError()
            if passed_map[checking_row][checking_col] == "X":
                if next_guard_rotation in coordinate_directions[checking_row, checking_col] or (next_next_guard_rotation in coordinate_directions[checking_row, checking_col] and step == 1 and map[checking_row+DIRECTION_VECTORS[next_guard_rotation][0]][checking_col+DIRECTION_VECTORS[next_guard_rotation][1]] == OBSTACLE):
                    print(f"Place obstacle at: {pos[0] + direction_vector[0]},{pos[1] + direction_vector[1]}")
                    placed_obstacles.append([pos[0] + direction_vector[0],pos[1] + direction_vector[1]])
                    return True
        except Exception as e:
            return False
        
def move(map: list, pos: list, direction_vector: list):
    global distinct_positions
    
    part2(map, pos, direction_vector)

    if not passed_map[pos[0] + direction_vector[0]][pos[1] + direction_vector[1]] == PASSED_CELL:
        passed_map[pos[0] + direction_vector[0]][pos[1] + direction_vector[1]] = PASSED_CELL
        distinct_positions += 1
    
    map[pos[0]][pos[1]] = "."
    map[pos[0] + direction_vector[0]][pos[1] + direction_vector[1]] = GUARD_ROTATIONS[current_guard_rotation]
    try:
        coordinate_directions[pos[0],pos[1]].append(current_guard_rotation)
    except:
        coordinate_directions[pos[0],pos[1]] = [current_guard_rotation]

    return [pos[0] + direction_vector[0], pos[1] + direction_vector[1]]

while True:
    move_allowed = movement_allowed(map, pos, direction_vector)
    if move_allowed == None:
        part2(map, pos, direction_vector)
        break
    elif move_allowed:
        pos = move(map, pos, direction_vector)
    else:
        direction_vector = rotate_guard(direction_vector)

print(f"Part 1: {distinct_positions}")
print(f"Part 2: {len(placed_obstacles)}")