import re

class Machine:
    def __init__(self, a: tuple, b: tuple, sum: tuple, cost_a: int = 3, cost_b: int = 1):
        self.a = a  # Movement of button A (xA, yA)
        self.b = b  # Movement of button B (xB, yB)
        self.sum = sum  # Goal position (x_goal, y_goal)
        self.cost_a = cost_a  # Cost of pressing Button A (in tokens)
        self.cost_b = cost_b  # Cost of pressing Button B (in tokens)

    def __str__(self):
        return f"Button A: {self.a}\nButton B: {self.b}\nSum: {self.sum}\nCost A: {self.cost_a}\nCost B: {self.cost_b}"

    def find_button_presses(self):
        min_cost = float('inf')  # Start with an infinitely large cost
        best_a_count = best_b_count = None  # Variables to store the best solution
        
        # Try different values for a_count (presses of Button A)
        for a_count in range(0, (self.sum[0] // self.a[0]) + 1):
            # Calculate b_count based on the Y-axis equation
            # y_goal = a[1] * a_count + b[1] * b_count => b_count = (y_goal - a[1] * a_count) / b[1]
            remaining_y = self.sum[1] - self.a[1] * a_count
            if remaining_y % self.b[1] == 0:  # Check if remaining_y is divisible by b[1]
                b_count = remaining_y // self.b[1]
                if b_count >= 0:  # Ensure b_count is non-negative
                    # Now check if this b_count satisfies the X-coordinate equation
                    if self.a[0] * a_count + self.b[0] * b_count == self.sum[0]:
                        # Calculate the total cost for this solution
                        total_cost = a_count * self.cost_a + b_count * self.cost_b
                        # If this solution is cheaper than previous ones, update the best solution
                        if total_cost < min_cost:
                            min_cost = total_cost
                            best_a_count = a_count
                            best_b_count = b_count

        # Return the best solution or None if no solution was found
        if best_a_count is not None and best_b_count is not None:
            return best_a_count, best_b_count, min_cost
        else:
            return None, None, None  # No solution found

def parse_input(file_path):
    machines = []
    buttonA = buttonB = sumTuple = None  # Initialize variables for each set of data

    with open(file_path, "r") as f:
        data = f.readlines()
        for line in data:
            if line.strip() == "":  # Empty line marks the end of one machine's data
                if buttonA and buttonB and sumTuple:
                    machines.append(Machine(buttonA, buttonB, sumTuple))
                buttonA = buttonB = sumTuple = None  # Reset for next machine
            elif line.startswith("Button A"):
                # Use regex to extract values after "X+" and "Y+"
                match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", line)
                if match:
                    buttonA = (int(match.group(1)), int(match.group(2)))
            elif line.startswith("Button B"):
                # Use regex to extract values after "X+" and "Y+"
                match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", line)
                if match:
                    buttonB = (int(match.group(1)), int(match.group(2)))
            elif line.startswith("Prize"):
                # Use regex to extract values after "X=" and "Y="
                match = re.match(r"Prize: X=(\d+), Y=(\d+)", line)
                if match:
                    sumTuple = (int(match.group(1)), int(match.group(2)))

        # Add the last machine after the loop
        if buttonA and buttonB and sumTuple:
            machines.append(Machine(buttonA, buttonB, sumTuple))

    return machines


# Example usage
machines = parse_input("13/small_input.txt")

sum_tokens = 0
# Now, process each machine and print the result
for mac in machines:
    a_press, b_press, min_cost = mac.find_button_presses()
    if min_cost is not None: sum_tokens += min_cost
    print(a_press, b_press, min_cost)

print(f"---\nTotal min cost: {sum_tokens}")