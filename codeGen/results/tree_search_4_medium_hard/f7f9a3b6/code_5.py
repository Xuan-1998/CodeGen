def alphabetIndex(c):
    return ord(c) - ord('a')

def countChars(s,a):
    return sum(1 for c in s if a[alphabetIndex(c)] > 0)

n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][i] = True

for i from 0 to n-2:
    for j from i+1 to n-1:
        if a[alphabetIndex(s[i])] > 0 and countChars(s[i+1:j+1],a) <= a[alphabetIndex(s[i])]:
            dp[i][j] = True
        elif dp[i-1][i] and dp[i][j]:
            dp[i][j] = True

ways_to_split = sum(1 for i in range(n+1) if dp[0][i])
longest_substring = max((j-i for i from 0 to n-2 for j from i+1 to n-1 if dp[i][j]),default=0)
min_substr_length = min((j-i for i from 0 to n-2 for j from i+1 to n-1 if dp[i][j]),default=n)

print(ways_to_split % (10**9 + 7))
print(longest_substring)
print(min_substr_length)
