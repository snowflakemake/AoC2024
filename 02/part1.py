lines = []
safeLines = []
unsafeLines = []

with open("02/input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())
        
for line in lines:
    cols = [int(x) for x in line.split()]
    sortedLine = sorted(cols)
    if sortedLine != cols and sortedLine != cols[::-1]:
        print(f"{line}: Neither strictly assending nor decending")
        unsafeLines.append(line)
        continue
    
    for i, col in enumerate(cols):
        if i != len(cols) - 1:
            if abs(col - cols[i+1]) < 1 or abs(col - cols[i+1]) > 3:
                unsafeLines.append(line)
                break
    else:
        safeLines.append(line)
        
print(f"Safe lines: {len(safeLines)}")