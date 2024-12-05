def RotateMatrix90(matrix):
    """
    Rotates matrix 90 degrees clockwise
    """
    rotatedMatrix = []

    for col_index in range(len(matrix[0])):
        column = [row[col_index] for row in matrix]
        rotatedMatrix.append(column[::-1])
    return rotatedMatrix

def checkCross(matrix, i0, i1):
    found_matches = 0
    if i0 >= len(matrix): return False
    if i0+2 >= len(matrix) or i1+2 >= len(matrix[i0]):
        return False
    
    MATCH_WORD = ['M', 'A', 'S']
    firstCell = matrix[i0][i1]
    if not firstCell in [MATCH_WORD[0], MATCH_WORD[-1]]:
        return False

    for i in range(4):
        if i > 0: matrix = RotateMatrix90(matrix)
        test_word = [matrix[i0][i1], matrix[i0+1][i1+1], matrix[i0+2][i1+2]]
        if test_word == MATCH_WORD: found_matches += 1
    
    if found_matches == 2:
        return True
    else:
        return False

test = [
    ['S','A','S'],
    ['M','A','S'],
    ['M','A','M']
]

letters = []
sum = 0

with open("04/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line_list = []
        for letter in line.strip():
            line_list.append(letter)
        letters.append(line_list)

totalLetters = len(letters) * len(letters[0])
counter = 1

for i0, row in enumerate(letters):
    for i1 in range(len(row)):
        print(f"Testing {counter} of {totalLetters}")
        counter+=1
        if checkCross(letters, i0, i1): sum += 1

print(f"Found {sum} correct crosses!")