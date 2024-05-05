import sys
from collections import Counter

def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    counter = Counter(s)
    unique_chars = sum(1 for c, count in counter.items() if count == 1)

    for i in range(1, n + 1):
        for j in range(min(i, unique_chars) + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                prev_unique_chars = 0
                for k in range(j - 1, i):
                    if s[k] not in counter or counter[s[k]] > a[ord(s[k].lower()) - 97]:
                        prev_unique_chars += 1
                    dp[i][j] += (dp[k][j - 1] * pow(26, j - 1, 10**9 + 7) % (10**9 + 7))
                dp[i][j] %= 10**9 + 7

    ways_to_split = dp[n][0]
    max_length = max(dp[i][1] for i in range(n + 1))
    min_substrs = sum((dp[i][1] - 1) // (10**9 + 7) for i in range(n + 1)) % (10**9 + 7)

    print(ways_to_split)
    print(max_length)
    print(min_substrs)

if __name__ == "__main__":
    solve()
