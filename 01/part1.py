lcolumn = []
rcolumn = []
distances = []

with open("input.txt", "r") as f:
    for line in f:
        l, r = line.split()
        lcolumn.append(int(l))
        rcolumn.append(int(r))

lcolumn.sort()
rcolumn.sort()

for i in range(len(lcolumn)):
    distances.append(abs(lcolumn[i] - rcolumn[i]))
    
print(f"Sum of the distances is: {sum(distances)}")