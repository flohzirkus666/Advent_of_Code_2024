import re


with open("puzzle3.txt", "r") as file:
    puzzle_input = file.read()

numbers = re.findall(r"(?<=mul\()\d{1,},\d{1,}(?=\))", puzzle_input)
sum = 0

for number in numbers:
    num1, num2 = number.split(",")
    sum += int(num1) * int(num2)

print(sum)
