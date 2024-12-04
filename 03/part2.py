import re

MUL_TOKEN = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
DO_TOKEN = "do()"
DONT_TOKEN = "don't()"

enable = True
text = ""
multiplications = []
sum = 0

with open("03/input.txt", "r") as f:
    text = f.read()

while text != "":
    if enable:
        stop_index = text.find(DONT_TOKEN)
        if stop_index == -1:
            multiplications.extend(re.findall(MUL_TOKEN, text))
            break
        enable = False
        multiplications.extend(re.findall(MUL_TOKEN, text[:stop_index]))
        text = text[stop_index:]
    else:
        start_index = text.find(DO_TOKEN)
        if start_index == -1:
            break
        enable = True
        text = text[start_index:]


for mul in multiplications:
    a, b = map(int, re.findall(r"[0-9]{1,3}", mul))
    sum += a*b

print(f"Sum: {sum}")