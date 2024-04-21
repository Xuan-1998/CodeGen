import sys

def calculate_probabilities(N, P):
    dp = [1.0] + [0.0] * N
    for i in range(1, N+1):
        if i >= 2:
            dp[i] += dp[i-2] * (P/100)
        if i >= 3:
            dp[i] += dp[i-3] * ((100-P)/100)
    return dp[N]

def main():
    T = int(input().strip())
    for _ in range(T):
        N, P = map(int, input().strip().split())
        probability = calculate_probabilities(N, P)
        print(f"{probability:.6f}")

if __name__ == "__main__":
    main()
