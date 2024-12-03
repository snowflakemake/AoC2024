lcolumn = []
rcolumn = []
sum = 0

with open("input.txt", "r") as f:
    for line in f:
        l, r = line.split()
        lcolumn.append(int(l))
        rcolumn.append(int(r))
        
# Create dictionary of ID occurrences in right column
id_counts = {}
for i, id in enumerate(rcolumn):
    if id in id_counts:
        id_counts[id] += 1
    else:
        id_counts[id] = 1
        
# Loop through left list to find occurences in right list
for id in lcolumn:
    if id in id_counts:
        sum += id_counts[id] * id
        print(f"[*] Added {id}*{id_counts[id]} -> Sum: {sum}")