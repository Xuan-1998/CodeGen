import sys

def main():
    # Read input
    n = int(input().strip())
    x = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))

    # Initialize dp array with infinity
    dp = [float('inf')] * (n + 2)
    dp[0] = dp[1] = 0  # No durability required for the first two points

    # For each point, calculate the maximum length it can support and update dp
    for i in range(2, n + 2):
        for j in range(i - 1, 0, -1):
            length = x[i - 1] - x[j - 1]
            if length <= d[j - 1]:
                dp[i] = min(dp[i], dp[j] + max(0, length - d[j - 1]))

    # The answer is the minimum durability required to prevent collapse
    answer = dp[-1] if dp[-1] != float('inf') else 0
    print(answer)

if __name__ == "__main__":
    main()
