def findSums():
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # Initialize the dp table with False values
    dp = [[False] * (sum(numbers) + 1) for _ in range(N + 1)]
    
    # Base case: An empty subset can always sum up to 0
    dp[0][0] = True
    
    # Fill up the dp table using a bottom-up approach
    for i in range(1, N + 1):
        for j in range(sum(numbers) + 1):
            if numbers[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - numbers[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Print out all distinct sums that can be generated
    unique_sums = set()
    for j in range(sum(numbers) + 1):
        if dp[N][j]:
            unique_sums.add(j)
    
    print(' '.join(map(str, sorted(unique_sums))))


if __name__ == "__main__":
    findSums()
