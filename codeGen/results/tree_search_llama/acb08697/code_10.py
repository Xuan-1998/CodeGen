n = int(input())
pile_size = 0
for op in input().split():
    if op == "+":
        pile_size += 1
    else:
        pile_size = max(0, pile_size - 1)
print(pile_size)
