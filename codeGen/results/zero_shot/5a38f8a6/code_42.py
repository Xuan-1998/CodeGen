def solution(n):
    if n ** 0.5 == int(n ** 0.5):  # n is a perfect square
        return 1
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = int(i ** 0.5) + 1
        for k in range(j):
            if i >= k ** 2:
                dp[i] = min(dp[i], dp[i - k ** 2] + 1)
    return dp[n]

if __name__ == "__main__":
    n = int(input())  # Read input from stdin
    print(solution(n))  # Print the result to stdout
