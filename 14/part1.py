import math


input_file = "14/input.txt"
map_height = 103
map_width = 101
seconds = 100
if "small" in input_file:
    map_height = 7
    map_width = 11

class Robot:
    def __init__(self, position: tuple, velocity: tuple):
        self.position = position  # (x, y)
        self.velocity = velocity  # (x, y)
    
    def move(self):
        global map_width, map_height
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        if self.position[0] < 0:
            self.position = (map_width + self.position[0], self.position[1])
        elif self.position[0] >= map_width:
            self.position = (self.position[0] - map_width, self.position[1])
        if self.position[1] < 0:
            self.position = (self.position[0], map_height + self.position[1])
        elif self.position[1] >= map_height:
            self.position = (self.position[0], self.position[1] - map_height)
            
        return self.position
    
def getQuadrant(pos: tuple):
    global map_width, map_height
    x = pos[0]
    y = pos[1]
    if x < map_width // 2 and y < map_height // 2:
        return 1
    elif x > map_width // 2 and y < map_height // 2:
        return 2
    elif x < map_width // 2 and y > map_height // 2:
        return 3
    elif x > map_width // 2 and y > map_height // 2:
        return 4
    else:
        return None
    
robots = []
positions = []
with open(input_file, "r") as f:
    for line in f.readlines():
        pos, vel = line.strip().split(" ")
        position = tuple(map(int, pos[2:].split(",")))
        velocity = tuple(map(int, vel[2:].split(",")))
        robots.append(Robot(position, velocity))

for i in range(seconds):
    positions = [robot.move() for robot in robots]

quadrants = [0 for _ in range(4)]
for pos in positions:
    if getQuadrant(pos) == None:
        continue
    quadrants[getQuadrant(pos) - 1] += 1

print(math.prod(quadrants))