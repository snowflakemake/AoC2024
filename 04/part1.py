MATCH_WORD = list('XMAS')
letters = []
sum = 0

with open("04/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line_list = []
        for letter in line.strip():
            line_list.append(letter)
        letters.append(line_list)

def PrintMatrix(matrix):
    for line in matrix:
        print(str(line))

def CountXMAS(matrix, reversed=False):
    """
    Counts occurences of MATCH_WORD in given matrix, only from left to right occurences
    """
    sum = 0
    for line in matrix:
        working_word = []
        if reversed: line = line[::-1]
        for letter in line:
            if letter == MATCH_WORD[len(working_word)]:
                working_word.append(letter)
                if working_word == MATCH_WORD:
                    sum += 1
                    working_word = []
            elif letter == MATCH_WORD[0]:
                working_word = [letter]
            else:
                working_word = []
    return sum

def RotateMatrix90(matrix):
    """
    Rotates matrix 90 degrees clockwise
    """
    rotatedMatrix = []

    for col_index in range(len(matrix[0])):
        column = [row[col_index] for row in matrix]
        rotatedMatrix.append(column[::-1])
    return rotatedMatrix

def RotateMatrix45(matrix):
    """
    Groups matrix elements into diagonals (Rotating 45 degrees).
    """
    rows, cols = len(matrix), len(matrix[0])
    diagonals = [[] for _ in range(rows + cols - 1)]
    
    for i in range(rows):
        for j in range(cols):
            diagonals[i + j].append(matrix[i][j])
    return diagonals

prevSum = sum
sum += CountXMAS(letters)                                                   # Left to Right
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(letters, reversed=True)                                    # Right to Left
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(RotateMatrix90(letters))                                   # Upwards
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(RotateMatrix90(letters), reversed=True)                    # Downwards
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(RotateMatrix45(letters))                                   # Low-Left to High-Right
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(RotateMatrix45(letters), reversed=True)                    # High-Right to Low-Left
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(RotateMatrix45(RotateMatrix90(letters)))                   # Low-Right to High-Left
print("Added:", sum-prevSum)
prevSum = sum
sum += CountXMAS(RotateMatrix45(RotateMatrix90(letters)), reversed=True)    # High-Left to Low-Right
print("Added:", sum-prevSum)
print(sum)