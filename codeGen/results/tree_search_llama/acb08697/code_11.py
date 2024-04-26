n = int(input())
s = input()

stones = 0
for op in s:
    stones += 1 if op == '+' else -1

print(stones)
