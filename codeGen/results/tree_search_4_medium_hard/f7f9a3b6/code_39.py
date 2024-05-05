import sys

n = int(input())
s = input()
a = list(map(int, input().split()))

dp_unique = [0] * (n + 1)
unique_chars = {}
for i in range(n):
    if s[i] not in unique_chars:
        unique_chars[s[i]] = 0
    unique_chars[s[i]] += 1

for i in range(1, n + 1):
    dp_unique[i] = max(dp_unique[i - 1], unique_chars.get(s[i - 1], 0) if s[i - 1] not in unique_chars else 0)

dp_repeated = [0] * (n + 1)
repeated_counts = {}
for i in range(26):
    repeated_counts[chr(ord('a') + i)] = a[i]

for i in range(n, 0, -1):
    for j in range(min(i, repeated_counts[s[i - 1]])):
        if not (i - j > dp_repeated[i - 1]):
            dp_repeated[i] = max(dp_repeated[i], dp_repeated[i - j] + j)
        else:
            dp_repeated[i] = max(dp_repeated[i], i)

num_ways = (dp_unique[n] * sum(1 for _ in range(n))) % (10**9 + 7)
longest_substring_length = max(max(unique_chars.values()), max(repeated_counts.values()))
min_substrings = min(min(unique_chars, key=unique_chars.get), min(repeated_counts, key=repeated_counts.get))

print(num_ways)
print(longest_substring_length)
print(min_substrings)
