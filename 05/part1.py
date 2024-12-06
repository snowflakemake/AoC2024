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

def get_middle(list):
    return list[int(len(list)/2)]

for update in updates:
    if check_update(update, rules):
        sum += int(get_middle(update))

print(f"Sum: {sum}")