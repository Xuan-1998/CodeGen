import sys

def solve():
    a, b = map(int, input().split())
    dp = [[0] * (31) for _ in range(315)]

    for i in range(1, 316):
        for j in range(i+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j-1]
                # Perform XOR with the left shift of b
                b_shifted = (b << 1)
                dp[i][j] ^= a & b_shifted

    result = sum(dp[i][i] for i in range(315)) % (10**9 + 7)
    print(result)

if __name__ == "__main__":
    solve()
