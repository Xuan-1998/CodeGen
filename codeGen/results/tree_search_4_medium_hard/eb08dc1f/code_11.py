import sys
n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(n+1)]

for i in range(10**n):
    digits = [int(x) for x in str(i)]
    for k in range(1, n+1):
        if all(digit == digits[0] for digit in digits[:k]):
            dp[k][digits[0]] += 1

result = []
for i in range(n+1):
    result.append(sum(dp[i]))

print(*result, sep=' ')
