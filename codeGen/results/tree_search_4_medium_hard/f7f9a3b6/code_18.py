import sys
from collections import defaultdict

a = list(map(int, input().split()))
s = input()
n = len(s)

mod = 10**9 + 7
dp_dict = {}

def dp(i, max_a):
    if (i, max_a) in dp_dict:
        return dp_dict[(i, max_a)]
    if i == n:
        return 1
    res = 0
    for j in range(i, min(n, i+a[ord(s[i])-97])):
        if s[i:j].isalpha():
            res += dp(j+1, min(max_a, a[ord(s[j])-97]))
        else:
            res += 1
    dp_dict[(i, max_a)] = res
    return res

ways = dp(0, a[ord(s[0])-97])
print(ways % mod)

max_len = 0
for i in range(n):
    for j in range(i+1, n+1):
        if s[i:j].isalpha():
            max_len = max(max_len, len(s[i:j]))
        else:
            break

min_substrs = float('inf')
for k in range(1, n+1):
    res = 0
    for i in range(n):
        j = min(n, i+a[ord(s[i])-97])
        if s[i:j].isalpha():
            res += dp(i+1, a[ord(s[i])-97])
        else:
            break
    if res > 0:
        min_substrs = min(min_substrs, k)
        break

print(max_len)
print(min_substrs)
