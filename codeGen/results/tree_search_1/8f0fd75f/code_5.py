import sys

def main():
    # Read input
    n = int(input())
    x = list(map(int, input().split()))
    d = list(map(int, input().split()))

    # Initialize the segments supported by each point
    segments = [x[i+1] - x[i] for i in range(n+1)]

    # Initialize the dp array with the durability of each point
    dp = [d[i] - segments[i] for i in range(n)]

    # Simulate the process of the ceiling collapsing
    for i in range(1, n):
        if dp[i-1] < 0:
            dp[i] += dp[i-1]

    for i in range(n-2, -1, -1):
        if dp[i+1] < 0:
            dp[i] += dp[i+1]

    # Find the minimum additional durability required
    min_additional_durability = min(dp)

    # If the minimum additional durability is negative, we need to add that much durability
    # If it is non-negative, we do not need to add a new point
    print(max(0, -min_additional_durability))

if __name__ == "__main__":
    main()
