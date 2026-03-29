import sys

def solve():
    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: binary representation of 0 does not contain consecutive ones.

    for i in range(1, n + 1):
        prev_binary = bin(i - 1)[2:]  # Convert integer to binary and remove the '0b' prefix.
        if all(x != y for x, y in zip(prev_binary.zfill(len(prev_binary) + 1), prev_binary[1:])):  # Check if previous bits are not consecutive ones.
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + (dp[i - 1] if i > 0 else 1)

    print(dp[n])

if __name__ == "__main__":
    solve()
