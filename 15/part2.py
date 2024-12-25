class Object:
    def __init__(self, position: tuple):
        """_summary_

        Args:
            position (tuple): (row, col)
        """
        self.row = position[0]
        self.col = position[1]

class MovableObject(Object):
    def allowMovement(self, direction: tuple, map, boxRecursive = False):
        """_summary_

        Args:
            direction (tuple): Movement as (row, col)
        """
        if not boxRecursive:
            if isinstance(self, LeftBox) or isinstance(self, RightBox):
                if not self.pair.allowMovement(direction, map, True): return False

        next_row = self.row + direction[0]
        next_col = self.col + direction[1]
        match str(map[next_row][next_col]):
            case ".":
                return True
            case "#":
                return False
            case "[" | "]":
                if isinstance(self, LeftBox) or isinstance(self, RightBox):
                    if map[next_row][next_col] == self.pair: return map[next_row][next_col].allowMovement(direction, map, True)
                    else: return map[next_row][next_col].allowMovement(direction, map)
                else: return map[next_row][next_col].allowMovement(direction, map)
    
    def move(self, direction: tuple, map, boxRecursive=False):
        next_row = self.row + direction[0]
        next_col = self.col + direction[1]
        if isinstance(map[next_row][next_col], MovableObject):
            map[next_row][next_col].move(direction, map)
        if (isinstance(self, LeftBox) or isinstance(self, RightBox)) and boxRecursive == False:
            if self.pair.row != next_row and self.pair.col != next_col:
                self.pair.move(direction, map, True)
        map[next_row][next_col] = self
        map[self.row][self.col] = Empty((self.row, self.col))
        self.row = next_row
        self.col = next_col

class Empty(Object):
    def __str__(self):
        return '.'

class Wall(Object):
    def __str__(self):
        return '#'
    
class Robot(MovableObject):
    def __str__(self):
        return '@'

class LeftBox(MovableObject):
    def __init__(self, position):
        super().__init__(position)
        right_position = (position[0], position[1] + 1)
        self.pair = RightBox(right_position, leftBox=self)
    def __str__(self):
        return '['
    def calcGps(self, map):
        self.gps = self.row * 100 + self.col
        return self.gps
        
class RightBox(MovableObject):
    def __init__(self, position, leftBox):
        super().__init__(position)
        self.pair = leftBox
    def __str__(self):
        return ']'
    def calcGps(self, map):
        return self.pair.calcGps(map)

def print_map(map):         
    for row in map:
        for col in row:
            print(col, end="")
        print()       


map = []
moves = []
robot = None
boxes = []

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
            x = 0
            for col in line:
                match col:
                    case "@":
                        robot = Robot((y, x))
                        map_row.append(robot)
                        map_row.append(Empty((y, x+1)))
                    case "O":
                        boxes.append(LeftBox((y, x)))
                        map_row.append(boxes[-1])
                        map_row.append(boxes[-1].pair)
                    case "#":
                        map_row.append(Wall((y, x)))
                        map_row.append(Wall((y, x+1)))
                    case ".":
                        map_row.append(Empty((y, x)))
                        map_row.append(Empty((y, x+1)))
                x += 2
            map.append(map_row)

for dir in moves:
    print_map(map)
    match dir:
        case "<":
            if robot.allowMovement((0, -1), map):
                robot.move((0, -1), map)
        case ">":
            if robot.allowMovement((0, 1), map):
                robot.move((0, 1), map)
        case "^":
            if robot.allowMovement((-1, 0), map):
                robot.move((-1, 0), map)
        case "v":
            if robot.allowMovement((1, 0), map):
                robot.move((1, 0), map)

print_map(map)
sum_box_gps = 0
for box in boxes:
    sum_box_gps += box.calcGps(map)
print(f"Sum of boxes gps: {sum_box_gps}")