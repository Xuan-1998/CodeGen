from sys import stdin

def has_consecutive_ones(n):
    return bin(n)[2:].count('1') > 0

dp = [0]
for i in range(1, int(stdin.readline()) + 1):
    dp.append(min(dp[-1], 1 + (not has_consecutive_ones(i))))
print(sum(1 for x in dp if not has_consecutive_ones(x)) - 1)
