import sys

def calculate_probability(N, P):
    if N == 1:
        return 0.0  # Can't reach position 1 with jumps of 2 or 3
    if N == 2:
        return P / 100.0  # Can only reach position 2 with one jump of 2

    dp = [0.0] * (N + 1)
    dp[0] = 1.0  # Starting position
    dp[2] = P / 100.0  # Can reach position 2 with one jump of 2

    for i in range(3, N + 1):
        dp[i] = (dp[i - 2] * P/100) + (dp[i - 3] * (100 - P)/100)

    return dp[N]

def main():
    T = int(input().strip())  # Read number of test cases
    for _ in range(T):
        N, P = map(int, input().strip().split())
        probability = calculate_probability(N, P)
        print(f"{probability:.6f}")

if __name__ == "__main__":
    main()
