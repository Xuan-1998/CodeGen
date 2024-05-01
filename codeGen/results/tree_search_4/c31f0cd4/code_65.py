from collections import defaultdict

def distinctSumSubarray(input_size, numbers):
    # Initialize DP array with dimensions (N+1, sum + 1)
    N = input_size
    total_sum = sum(numbers)
    dp = [[[] for _ in range(total_sum + 1)] for _ in range(N + 1)]

    # Base case: empty subset generates only one sum, 0
    dp[0][0] = [0]

    for i in range(1, N + 1):
        for j in range(total_sum + 1):
            if numbers[i - 1] <= j:
                # Calculate the new subset size by removing the current element from current_subset
                new_subset_size = i

                # Calculate the new sum by adding the current element to current_sum
                new_sum = j - numbers[i - 1]

                for subsum in dp[i - 1][new_sum]:
                    if subsum not in dp[new_subset_size][j]:
                        dp[new_subset_size][j].append(subsum)
            else:
                dp[i][j] = dp[i - 1][j]

    return set([sum(x) for x in dp[N]])


# Example usage
input_size = int(input())
numbers = list(map(int, input().split()))
print(*distinctSumSubarray(input_size, numbers), sep=' ')
