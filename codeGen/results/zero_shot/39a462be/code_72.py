import sys

A = [c for c in sys.stdin.readline().strip()]
B = [c for c in sys.stdin.readline().strip()]

A.sort()
B.sort()

all_substrs = []
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        all_substrs.append(''.join(A[i:j]))

for i in range(len(B)):
    for j in range(i + 1, len(B) + 1):
        all_substrs.append(''.join(B[i:j]))

def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

score = 0
for a in all_substrs:
    for b in all_substrs:
        lcs_len = lcs(a, b)
        score = max(score, 4 * lcs_len - (len(a) + len(b)))

print(score)
