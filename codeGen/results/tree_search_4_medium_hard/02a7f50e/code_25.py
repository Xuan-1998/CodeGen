from collections import defaultdict

n = int(input())
memo = defaultdict(int)
for _ in range(n):
    pos, power = map(int, input().split())
    for j in range(power, -1, -1):
        memo[(pos, j)] = min((k-1, max(0, j-1)) + 1 for k in range(pos+1) if (k, j-1) not in memo)
print(memo[(n-1, 0)])
