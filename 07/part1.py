lines = []
sum = 0

with open("07/input.txt", "r") as f:
    for line in f.readlines():
        test_value = int(line.split(":")[0])
        computing_values = [int(x) for x in line.split(":")[1].strip().split()]
        lines.append([test_value, computing_values])

def try_operands(test_value: int, computing_values: list) -> bool:
    if not computing_values:
        return False
    
    num_operators = len(computing_values) - 1
    total_combinations = 2 ** num_operators

    for i in range(total_combinations):
        operations = []
        for j in range(num_operators):
            if(i >> j) & 1:
                operations.append('+')
            else:
                operations.append('*')

        result = computing_values[0]

        for k, op in enumerate(operations):
            if op == '+':
                result += computing_values[k + 1]
            elif op == '*':
                result *= computing_values[k + 1]
        
        if result == test_value:
            print(test_value, operations)
            return True
        
    return False
for line in lines:
    if try_operands(line[0], line[1]):
        sum += line[0]

print(f"Sum: {sum}")