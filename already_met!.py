print("enter 'Z' to stop")
x = input()
length = 0
numbers = set()
while x != 'Z':
    x = int(x)
    length = len(numbers)
    numbers.add(x)
    if length == len(numbers):
        print(x, "already met")
    x = input()