# Read input
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Preprocess the string
freq = {}
for char in s:
    if char not in freq:
        freq[char] = 0
    freq[char] += 1

# Dynamic Programming
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n):
    for j in range(i+1, n+1):
        if all(freq[char] <= a[ord(char)-97] for char in s[i-j:i]):
            dp[i][j] = (dp[i-1][i-1] if i > 0 else 1) + dp[i-1][j-1]
        else:
            dp[i][j] = 0

# Calculate results
ways = sum(dp[-1])
max_length = max(i for i in range(1, n+1) if dp[-1][i])
min_substrings = min(i for i in range(1, n+1) if dp[-1][i])

print(ways % (10**9 + 7))
print(max_length)
print(min_substrings)
