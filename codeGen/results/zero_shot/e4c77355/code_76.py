n = int(input())  # read the input array size from stdin
arr = list(map(int, input().split()))  # read the input array from stdin
dp = [0] * n  # initialize the dp table with zeros

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_lis_length = max(dp)
print(max_lis_length)  # print the result to stdout
