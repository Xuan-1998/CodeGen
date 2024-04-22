import sys

def calculate_probability(N, P):
    if N == 1:
        return 0.0
    if N == 2:
        return P / 100.0

    dp = [0.0] * (N + 1)
    dp[0] = 1.0
    dp[2] = P / 100.0

    for i in range(3, N + 1):
        dp[i] = (dp[i - 2] * P / 100.0) + (dp[i - 3] * (100 - P) / 100.0)

    return dp[N]

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N, P = map(int, sys.stdin.readline().strip().split())
        probability = calculate_probability(N, P)
        print(f"{probability:.6f}")

if __name__ == "__main__":
    main()
