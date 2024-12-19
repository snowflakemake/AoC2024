map = []
areas = {}
visited_coords = set()  # Use a set for global visited coordinates

class Area:
    def __init__(self, letter, row, col):
        self.code = letter
        self.area = 1
        self.perimeter = 0
        self.sides = 0
        self.coords = (row, col)
        self.all_coords = [self.coords]

    def findNeighbors(self, map, visited_coords):
        check_next = [self.coords]  # Start with the initial position
        visited_coords.add(self.coords)
        
        # Explore neighbors
        while check_next:
            current = check_next.pop(0)            
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Up, Left, Down, Right
            for dir in directions:
                next_row = current[0] + dir[0]
                next_col = current[1] + dir[1]
                
                # Check boundaries
                if not (0 <= next_row < len(map) and 0 <= next_col < len(map[0])):
                    continue
                
                # Check if already visited
                if (next_row, next_col) in visited_coords:
                    continue
                
                # Check if cell matches the target code
                if map[next_row][next_col] == self.code:
                    visited_coords.add((next_row, next_col))
                    self.area += 1  # Assuming self.area tracks the size of the region
                    check_next.append((next_row, next_col))
                    self.all_coords.append((next_row, next_col))
        
        return visited_coords  # Return the updated visited coordinates

    def getPerimeter(self, map):
        # Calculate the perimeter based on all_coords
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Up, Left, Down, Right
        for coord in self.all_coords:
            row, col = coord
            for dir in directions:
                next_row = row + dir[0]
                next_col = col + dir[1]
                
                # If out of bounds or neighbor is not part of the area, increment perimeter
                if not (0 <= next_row < len(map) and 0 <= next_col < len(map[0])) or map[next_row][next_col] != self.code:
                    self.perimeter += 1
        
        return self.perimeter

    def calculateSides(self, map):
        visited_sides = set()  # To track unique sides
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Up, Left, Down, Right
        
        def trace_side(start, direction):
            """Trace a continuous side starting from a boundary."""
            side = set()  # Track all cells contributing to this side
            current = start
            while True:
                side.add(current)
                next_row, next_col = current[0] + direction[0], current[1] + direction[1]
                if (next_row, next_col) not in self.all_coords:  # Hit boundary or different region
                    break
                current = (next_row, next_col)
            return side

        for coord in self.all_coords:
            row, col = coord
            for dir in directions:
                next_row = row + dir[0]
                next_col = col + dir[1]
                
                # If boundary or different region
                if not (0 <= next_row < len(map) and 0 <= next_col < len(map[0])) or map[next_row][next_col] != self.code:
                    start_edge = (row, col, dir)  # Boundary start and direction
                    if start_edge not in visited_sides:
                        side = trace_side((row, col), dir)
                        visited_sides.update(side)  # Mark side as visited

        self.sides = len(visited_sides)
        return self.sides

# Read the map from the file
with open("12/small_input.txt", "r") as f:
    for line in f.readlines():
        row = []
        for col in line.strip():
            row.append(col)
        map.append(row)

total_price = 0
# Find areas
for y, row in enumerate(map):
    for x, col in enumerate(row):
        if (y, x) in visited_coords: 
            continue  # Skip already visited cells
        area = Area(col, y, x)
        visited_coords = area.findNeighbors(map, visited_coords)  # Pass the global visited set
        area.getPerimeter(map)
        area.calculateSides(map)
        score = area.area * area.sides
        total_price += score
        print(f"{area.code}:\n Parameter: {area.perimeter}\n Sides: {area.sides}\n Area: {area.area}\n Score: {score}", end="\n\n")

print("Total price:",total_price)
