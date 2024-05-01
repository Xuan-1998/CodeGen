def max_points(a):
    n = len(a)
    dp = {0: 0}  # base case

    for i in range(1, n):
        if a[i] - 1 not in dp or a[i] + 1 not in dp:
            dp[i] = max(dp.get(i-1, 0), dp.get(i-2, 0)) + 1
        else:
            dp[i] = max(dp[i-1], dp[i-2]) + 1

    return max(dp.values())

# Example usage:
n = int(input())  # read number of integers in the sequence
a = [int(x) for x in input().split()]  # read the sequence
print(max_points(a))  # output the maximum number of points earned
