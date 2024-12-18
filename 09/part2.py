# Should work, just takes alooooooooooooong time...

text_input = []
storage = {}

with open("09/input.txt", "r") as f:
    for line in f.readlines():
        for carachter in line.strip():
            text_input.append(carachter)

data_block_counter = 0
storage_index = 0
for i, digit in enumerate(text_input):
    storage_block = []
    if i % 2 == 0:
        for j in range(int(digit)):
            storage_block.append(data_block_counter)
        storage[storage_index] = storage_block
        storage_index += len(storage_block)
        data_block_counter += 1
    else:
        for j in range(int(digit)):
            storage_block.append('.')
        storage[storage_index] = storage_block
        storage_index += len(storage_block)

# Sort storage space 
keys = list(storage.keys())
reversed_data_keys = keys
reversed_data_keys.reverse()
reversed_data_keys = [key for key in reversed_data_keys if '.' not in storage[key]]

index = len(keys)

def find_available_space(storage: dict, data_key: int):
    if data_key not in storage: return None
    for key in storage.keys():
        if key >= data_key: continue
        if storage[key][0] == '.':
            if len(storage[key]) >= len(storage[data_key]):
                return key
    return None

def move_data(storage, data_key: int, space_key: int):
    # Debugging storage before operations
    print(f"Initial storage: {storage}")
    
    # Retrieve the data to move
    data = storage[data_key]
    space_length = len(storage[space_key])  # Length of the target space
    
    print(f"[*] Moving data from key {data_key} to {space_key}")
    print(f"    Data: {data}")
    print(f"    Target space before move: {storage[space_key]}")
    print(f"    Space difference: {space_length - len(data)}")
    
    # Move data
    storage[space_key] = data
    storage[data_key] = ['.'] * (len(data))
    
    # Check and handle space difference
    if len(data) < space_length:
        filler_key = space_key + len(data)
        filler_value = ['.'] * (space_length - len(data))
        print(f"Adding filler key {filler_key} with value {filler_value}")
        
        # Update storage with filler data
        storage[filler_key] = filler_value
        
        # Confirm addition of filler
        if filler_key in storage:
            print(f"Key {filler_key} successfully added with value: {storage[filler_key]}")
        else:
            print(f"Failed to add key {filler_key}")
    
    # Debugging storage after operations
    print(f"Updated storage: {storage}")
    return storage


for data_key in reversed_data_keys:
    print(f"Moving key: %s" % data_key)
    if storage[data_key][0] == '.': continue
    available_space_key = find_available_space(storage, data_key)
    if available_space_key is not None:
        storage = move_data(storage, data_key, available_space_key)
        storage = dict(sorted(storage.items()))


for value in storage.values():
    for val in value:
        print(val, end='')

checksum = 0      
for key in storage.keys():
    if storage[key][0] == '.': continue
    checksum += storage[key][0] * key