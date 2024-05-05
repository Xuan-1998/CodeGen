import sys

def solve(s, a):
    n = len(s)
    mod = 10**9 + 7
    ways = [0] * (n + 1)
    max_len = 0
    min_substrings = n

    for i in range(n):
        count = 0
        j = i
        while j < n and s[j].count(s[i]) <= a[ord(s[i]) - ord('a')]:
            count += 1
            j += 1
        ways[i + 1] = (ways[i] + count) % mod
        max_len = max(max_len, count)
        min_substrings = min(min_substrings, count)

    return ways[-1], max_len, min_substrings

n = int(input())
s = input()
a = list(map(int, input().split()))

print(solve(s, a))
