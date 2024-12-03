safeLines = []
unsafeLines = []

def isStrictlyOrdered(cols):
    sortedCols = sorted(cols)
    return sortedCols == cols or sortedCols == cols[::-1]

def checkSafeSteps(cols):
    for i, col in enumerate(cols):
        if i != len(cols) - 1:
            if abs(col - cols[i+1]) < 1 or abs(col - cols[i+1]) > 3:
                return False
    else:
        return True

def checkSafe(line, iteration=False):
    cols = [int(x) for x in line.split()]
    
    if isStrictlyOrdered(cols):
        if checkSafeSteps(cols):
            return True
        elif not iteration:
            for i in range(0, len(cols) - 1):
                if checkSafe(" ".join(map(str, cols[:i] + cols[i+1:])), iteration=True):
                    return True
            else:
                return checkSafe(" ".join(map(str, cols[:len(cols) - 1])), iteration=True)
        else:
            return False
    elif not iteration:
            for i in range(0, len(cols) - 1):
                if checkSafe(" ".join(map(str, cols[:i] + cols[i+1:])), iteration=True):
                    return True
            else:
                return checkSafe(" ".join(map(str, cols[:len(cols) - 1])), iteration=True)
    else:
        return False

# Read input lines
lines = []
with open("02/input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

# Check each line for safety
for line in lines:
    print(f"Checking {line:<30}", end=": ")
    if checkSafe(line):
        print("Safe")
        safeLines.append(line)
    else:
        print("Unsafe")
        unsafeLines.append(line)

# Print results
print(f"Safe lines count: {len(safeLines)}")