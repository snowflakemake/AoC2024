map = []
passed_map = []
pos = []
GUARD_ROTATIONS = ['^','>','v','<']
current_guard_rotation = '^'
PASSED_CELL = "X"
OBSTACLE = "#"
direction_vector = [-1, 0]
distinct_positions = 0

with open("06/input.txt", "r") as f:
    lines = f.readlines()
    for row, line in enumerate(lines):
        line_list = []
        for col, letter in enumerate(line.strip()):
            line_list.append(letter)
            if letter in GUARD_ROTATIONS: 
                pos = [row, col]
                current_guard_rotation = letter
        map.append(line_list)
        passed_map.append(['.' for i in range(len(line_list))])

def movement_allowed(map: list, pos: list, direction_vector: list):
    next_pos = [pos[0] + direction_vector[0], pos[1] + direction_vector[1]]
    if next_pos[0] >= len(map) or next_pos[1] >= len(map[0]) or next_pos[0] < 0 or next_pos[1] < 0:
        return None
    return not map[next_pos[0]][next_pos[1]] == OBSTACLE

def rotate_guard(direction_vector: list):
    global current_guard_rotation
    match direction_vector:
        case [-1,0]:
            current_guard_rotation = GUARD_ROTATIONS[1]
            return [0,1]
        case [0,1]:
            current_guard_rotation = GUARD_ROTATIONS[2]
            return [1,0]
        case [1,0]:
            current_guard_rotation = GUARD_ROTATIONS[3]
            return [0,-1]
        case [0,-1]:
            current_guard_rotation = GUARD_ROTATIONS[0]
            return [-1,0]

def move(map: list, pos: list, direction_vector: list):
    global distinct_positions
    if not passed_map[pos[0] + direction_vector[0]][pos[1] + direction_vector[1]] == PASSED_CELL:
        passed_map[pos[0] + direction_vector[0]][pos[1] + direction_vector[1]] = PASSED_CELL
        distinct_positions += 1

    map[pos[0]][pos[1]] = "."
    map[pos[0] + direction_vector[0]][pos[1] + direction_vector[1]] = current_guard_rotation

    return [pos[0] + direction_vector[0], pos[1] + direction_vector[1]]

while True:
    move_allowed = movement_allowed(map, pos, direction_vector)
    if move_allowed == None:
        break
    elif move_allowed:
        pos = move(map, pos, direction_vector)
    else:
        direction_vector = rotate_guard(direction_vector)

print(distinct_positions)