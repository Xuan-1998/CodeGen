import sys

n, k = map(int, input().split())
s = input()

result = s[:k]

# If the length of the original string is shorter than k,
# delete the last character if it's lexicographically smaller
if len(s) < k:
    for i in range(k - len(s)):
        if result[i] > s[-1]:
            result += s[-1]
        else:
            result = result[:i] + s[-1] + result[i:]

print(result)
