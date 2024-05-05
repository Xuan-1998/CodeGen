===BEGIN PLAN===
1. Base case: If the array is empty, return 0.
2. Initialize a 2D table dp of size n x m, where n is the length of the input array and m is a constant (e.g., 10000). Fill all elements in dp with -1.
3. Iterate through each element in the input array.
4. For each element at index i:
   a. Calculate the length of the longest increasing subsequence ending at that position by comparing it to all previous elements and updating dp[i][j] accordingly.
   b. Store this updated state in dp[i][j].
5. Return the maximum value from dp[n-1][m-1].

Updated Plan:

==Code==
n = int(input())
arr = [int(x) for x in input().split()]
dp = [[0]*25 for _ in range(n)]

for i in range(n):
    for j in range(25):
        if arr[i] <= j:
            dp[i][j] = max(dp[i-1][k]+1 if 0<=k<j else 0 for k in range(j))
        else:
            dp[i][j] = 1

print(max(dp[-1]))
