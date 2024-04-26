n = int(input())
operations = input()

x = 0
min_stones = float('inf')

for op in operations:
    if op == '+':
        x += 1
    else:
        x -= 1
    min_stones = min(min_stones, x)

print(min_stones)
