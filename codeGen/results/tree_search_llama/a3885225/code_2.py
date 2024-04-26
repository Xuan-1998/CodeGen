ones = 0
for c in input():
    ones += int(c)

print("YES" if ones >= len(input()) // 2 else "NO")
