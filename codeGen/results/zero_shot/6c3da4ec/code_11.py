import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    # Initialize dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # Calculate the bitwise OR of two substrings
            or_val = int(s[i - 1:j], 2)
            if i == 1:
                dp[0][j] = or_val
            else:
                for k in range(j):
                    dp[k][i].extend([or_val, dp[k][i - 1]])
            # Update the maximum value
            dp[i][j] = max(dp[i][j], dp[i - 1][k] | dp[0][j])

    # Print the maximum possible value
    print(bin(max([max(subarray) for subarray in dp]))[2:].zfill(n).upper())

if __name__ == "__main__":
    solve()
