import re

MUL_TOKEN = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

text = ""
multiplications = []
sum = 0

with open("03/input.txt", "r") as f:
    text = f.read()

multiplications = re.findall(MUL_TOKEN, text)

for mul in multiplications:
    a, b = map(int, re.findall(r"[0-9]{1,3}", mul))
    sum += a*b

print(f"Sum: {sum}")