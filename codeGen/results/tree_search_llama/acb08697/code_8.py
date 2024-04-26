n = int(input())
operations = input()

stones = 0

for op in operations:
    if op == "+":
        stones += 1
    elif op == "-":
        if stones > 0:
            stones -= 1

print(stones)
