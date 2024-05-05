import sys

n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i):
        if all(freq[chr(x)] <= a[x - 97] for x in range(ord(chr(j)), ord(chr(i))) % 26):
            dp[i] += dp[j]
    dp[i] %= 10**9 + 7

max_length = 0
for i in range(n + 1):
    if dp[i] > 0:
        max_length = max(max_length, i)
min_substrings = n // max_length

print(dp[n] % (10**9 + 7))
print(max_length)
print(min_substrings)

