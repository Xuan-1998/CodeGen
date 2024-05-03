import sys

def can_make_zero(n, arr):
    # Create a boolean array dp where dp[i] represents whether it is possible to make all elements of the subarray [0..i]
    # equal to zero.
    dp = [False] * (n + 1)

    # Base case: If all elements in the subarray [0..0] are already 0, return True.
    dp[0] = True

    for i in range(1, n + 1):
        if arr[i - 1] > 0:
            # If the current element is greater than 0, then we have two choices: decrement it and move to the next element
            # or skip it and move to the previous element. In this case, return False.
            dp[i] = any(dp[j] for j in range(i)) if i > 1 else False
        else:
            # If the current element is 0, then we can simply move to the next element.
            dp[i] = dp[i - 1]

    # Return whether it is possible to make all elements of the original array equal to zero.
    return dp[n]


# Read input from standard input
n = int(input())
arr = list(map(int, input().split()))

# Print the answer to standard output
print("YES" if can_make_zero(n, arr) else "NO")
