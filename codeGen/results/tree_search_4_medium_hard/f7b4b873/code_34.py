import sys

def is_palindrome(s):
    return s == s[::-1]

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

dp = [[False] * (len(S) + 1) for _ in range(len(S) + 1)]
partitioned_palindromes = []

for i in range(N):
    for j in range(i, N):
        if is_palindrome(S[i:j+1]):
            dp[i][j] = True
            partitioned_palindromes.append([S[i:j+1]])
        else:
            dp[i][j] = False

print(partitioned_palindromes)
