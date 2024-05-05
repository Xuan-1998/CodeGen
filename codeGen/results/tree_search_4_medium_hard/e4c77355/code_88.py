n = int(input())  # read input
arr = list(map(int, input().split()))  # read array

dp = [1] * n  # initialize dp table with all ones (single elements are increasing subsequences of length 1)

for i in range(1, n):
    for j in range(i):  # consider previous elements
        if arr[j] < arr[i]:  # new increasing subsequence ending at arr[i]
            dp[i] = max(dp[i], dp[j] + 1)  # update dp table

print(max(dp))  # print the maximum length of a longest increasing subsequence
