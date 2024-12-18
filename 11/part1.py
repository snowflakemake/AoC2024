# For part 2: Changing blinks to 75 doesn't do the trick.. although a stone value will always
# evolve in the same way, so its possible to predict the string.. i just don't bother right now...

input_line = ""

blinks = 25

with open("11/input.txt", "r") as f:
    input_line = f.readline().strip()
    
def blink(line: str) -> str:
    new_line = ""
    for stone in line.split(" "):
        # Rule 1: If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if int(stone) == 0:
            new_line += "1 "
        # Rule 2: If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
        # The left half of the digits are engraved on the new left stone, and the right half of the digits are 
        # engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif len(stone)%2 == 0:
            break_index = len(stone) // 2
            left_half = stone[:break_index]
            right_half = stone[break_index:]
            new_line += str(int(left_half)) + " " + str(int(right_half)) + " "
        # Rule 3: If none of the other rules apply, the stone is replaced by a new stone; 
        # the old stone's number multiplied by 2024 is engraved on the new stone.
        else:
            new_line += str(int(stone) * 2024) + " "
    return new_line.strip()

for _ in range(blinks):
    print(_ + 1)
    input_line = blink(input_line)
    
print(len(input_line.split(" ")))