input = []
storage = []
free_storage_positions = []

with open("09/input.txt", "r") as f:
    for line in f.readlines():
        for carachter in line.strip():
            input.append(carachter)

data_block_counter = 0
storage_index = 0
for i, digit in enumerate(input):
    if i % 2 == 0:
        for j in range(int(digit)):
            storage.append(data_block_counter)
            storage_index += 1
        data_block_counter += 1
    else:
        for j in range(int(digit)):
            storage.append('.')
            free_storage_positions.append(storage_index)
            storage_index += 1

# Sort storage space            
for i in range(len(storage) - 1, 0, -1):
    if len(free_storage_positions) == 0:
        break
    if storage[i] != '.' and free_storage_positions[0] < i:
        storage[free_storage_positions.pop(0)] = storage.pop(i)
        storage.append('.')
        if i not in free_storage_positions:
            free_storage_positions.append(i)
            free_storage_positions.sort()

# Calculate checksum
sum = 0      
for i in range(len(storage)):
    if storage[i] == '.':
        break
    sum += i*storage[i]

print(sum)