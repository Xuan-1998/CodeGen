n = int(input())
operations = input()

pile_size = 0

for op in operations:
    if op == '+':
        pile_size += 1
    else:
        pile_size -= 1

print(pile_size)
