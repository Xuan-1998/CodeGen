from sys import stdin

def longest_increasing_subsequences():
    arr = list(map(int, stdin.readline().split()))
    n = len(arr)

    # Initialize DP array with zeros
    dp = [0] * (n + 1)
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Count the number of maximum length subsequences
    return sum(1 for x in dp[1:] if x == max(max(dp)))

if __name__ == "__main__":
    print(longest_increasing_subsequences())
