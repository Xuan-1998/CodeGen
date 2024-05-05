def valid_split_point(s, i, a):
    for j in range(i - 1, -1, -1):
        if sum(ord(c) - ord('a') + 1 <= a[ord(c) - ord('a')] for c in s[j:i+1]) > a[ord(s[i]) - ord('a')]:
            return False
    return True

n = int(input())
s = input()
a = [int(x) for x in input().split()]

ways = 0
max_len = 0
min_substrs = float('inf')

for i in range(1, n):
    if valid_split_point(s, i, a):
        ways += 1
        max_len = max(max_len, len(substring(s, 0, i)))
        min_substrs = min(min_substrs, (i + 1) // (a[ord(s[i]) - ord('a')] + 1))

print(ways % (10**9 + 7))
print(max_len)
print(min_substrs)
