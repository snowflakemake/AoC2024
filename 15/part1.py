map = []
moves = []
robot = None
boxes = []

class Box:
    def __init__(self, position: tuple):
        """_summary_

        Args:
            position (tuple): (row, col)
        """
        self.row = position[0]
        self.col = position[1]
        self.gps = self.row * 100 + self.col
    def __str__(self):
        return 'O'        
    def updateGPS(self):
        self.gps = self.row * 100 + self.col
    def move(self, direction: tuple):
        global map
        """_summary_

        Args:
            direction (tuple): Movement as (row, col)
        """
        next_row = self.row + direction[0]
        next_col = self.col + direction[1]
        match str(map[next_row][next_col]):
            case ".":
                map[next_row][next_col] = self
                map[self.row][self.col] = "."
                self.row = next_row
                self.col = next_col
                self.updateGPS()
                return True
            case "#":
                return False
            case "O":
                allowed = map[next_row][next_col].move(direction)
                if allowed:
                    map[next_row][next_col] = self
                    map[self.row][self.col] = "."
                    self.row = next_row
                    self.col = next_col
                    self.updateGPS()
                    return True
                else:
                    return False
                
class Robot:
    def __init__(self, position: tuple):
        """_summary_

        Args:
            position (tuple): (row, col)
        """
        self.row = position[0]
        self.col = position[1]
    def __str__(self):
        return '@'
        
    def move(self, direction: tuple):
        global map
        """_summary_

        Args:
            direction (tuple): Movement as (row, col)
        """
        next_row = self.row + direction[0]
        next_col = self.col + direction[1]
        match str(map[next_row][next_col]):
            case ".":
                map[next_row][next_col] = self
                map[self.row][self.col] = "."
                self.row = next_row
                self.col = next_col
                return True
            case "#":
                return False
            case "O":
                allowed = map[next_row][next_col].move(direction)
                if allowed:
                    map[next_row][next_col] = self
                    map[self.row][self.col] = "."
                    self.row = next_row
                    self.col = next_col
                    return True
                else:
                    return False

with open("15/input.txt", "r") as f:
    movement = False
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        if line == "":
            movement = True
            continue
        if movement:
            for col in line:
                moves.append(col)
        else:
            map_row = []
            for x, col in enumerate(line):
                if col == "@":
                    robot = Robot((y, x))
                    map_row.append(robot)
                elif col == "O":
                    boxes.append(Box((y, x)))
                    map_row.append(boxes[-1])
                else:
                    map_row.append(col)
            map.append(map_row)
 
def print_map(): 
    global map          
    for row in map:
        for col in row:
            print(col, end="")
        print()       

for dir in moves:
    match dir:
        case "<":
            robot.move((0, -1))
        case ">":
            robot.move((0, 1))
        case "^":
            robot.move((-1, 0))
        case "v":
            robot.move((1, 0))

print_map()
sum_box_gps = 0
for box in boxes:
    sum_box_gps += box.gps
print(f"Sum of boxes gps: {sum_box_gps}")