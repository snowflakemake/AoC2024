rules = []
updates = []
lines = []
sum = 0

# Read input file
with open("05/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# Append rules and find breakpoint
for i, line in enumerate(lines):
    if line == '': 
        BREAKPOINT_INDEX = i
        break
    x, y = line.split("|")
    rules.append([x.strip(), y.strip()])

# Append updates
for update in lines[BREAKPOINT_INDEX + 1:]:
    updates.append(update.split(","))

def find_dependencies(id, rules):
    dependencies = []
    for rule in rules:
        if rule[1] == id:
            dependencies.append(rule[0])
    
    return dependencies

def check_update(update, rules):
    for i, part in enumerate(update):
        dependencies = find_dependencies(part, rules)
        for dep in dependencies:
            if dep in update[i:]:
                return False
    
    return True

'''
# My first try of sorting.. didn't really go as planned
# since it will loop pretty much forever, if not actually forever
def sort_update(update, rules):
    while True:
        for i, part in enumerate(update):
            dependencies = find_dependencies(part, rules)
            for dep in dependencies:
                if dep in update:
                    update.pop(update.index(dep))
                    update.insert(i, dep)
        if check_update(update, rules): break

    return update
'''

from collections import defaultdict, deque

def sort_with_dependencies(update, rules):
    # Build a graph and in-degree count from the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Create graph edges and in-degrees
    for a, b in rules:  # Rule: 'a' must come before 'b'
        if a in update and b in update:  # Only consider rules involving nodes in 'update'
            graph[a].append(b)
            in_degree[b] += 1
            if a not in in_degree:
                in_degree[a] = 0

    # Initialize the queue with elements having no dependencies
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    # Keep track of nodes we've seen to handle remaining nodes in 'update'
    seen = set()

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        seen.add(current)

        # Decrease the in-degree of dependent nodes
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # Add to queue if no dependencies remain
                queue.append(neighbor)

    # Add any remaining nodes in 'update' that weren't processed (e.g., due to cycles)
    for node in update:
        if node not in seen:
            sorted_order.append(node)

    return sorted_order



def get_middle(list):
    return list[int(len(list)/2)]

for update in updates:
    if not check_update(update, rules):
        print(update)
        update = sort_with_dependencies(update, rules)
        sum += int(get_middle(update))

print(f"Sum: {sum}")