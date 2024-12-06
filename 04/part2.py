def checkCross(matrix, i0, i1):
    found_matches = 0
    MATCH_WORD = [['M', 'A', 'S'], ['S','A','M']]
    directions = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]  # Diagonalriktning

    if i0 + 2 >= len(matrix) or i1 + 2 >= len(matrix[0]):
        return False

    for i in range(2):  # Loop för att rotera koordinaterna
        test_word = [matrix[i0 + dx][i1 + dy] for dx, dy in directions[i]]
        if test_word in MATCH_WORD: found_matches += 1
        if found_matches == 2: return True
    return False

test = [
    ['S','A','S'],
    ['M','A','S'],
    ['M','A','M']
]

letters = []

with open("04/input.txt", "r") as f:
    letters = [list(line.strip()) for line in f]

totalLetters = len(letters) * len(letters[0])
sum_matches = 0
counter = 1

for i0, row in enumerate(letters):  # Enumerate over rows
    for i1 in range(len(row)):  # Iterate over columns
        print(f"Testing {counter} of {totalLetters}")
        if checkCross(letters, i0, i1):
            sum_matches += 1
        counter += 1  # Increment counter for each test

print(f"Found {sum_matches} correct crosses!")
