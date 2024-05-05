def isLadder(arr, i, j):
    if i > j:  # base case: empty subsegment
        return True

    max_length = dp.get(i-1, 0)  # get the length of the longest non-decreasing subsequence ending at index i-1
    for k in range(i, j):  # iterate over indices from i to j-1
        if arr[k] <= arr[j]:  # check if the current element is not greater than the last element
            max_length = max(max_length, dp.get(k, 0))  # update the maximum length
    return max_length > 0 and all(arr[i:j+1])  # check if the subsegment is a ladder

dp = {}  # memoization dictionary
n, m = map(int, input().split())  # read input
arr = list(map(int, input().split()))  # read array
for _ in range(m):
    l, r = map(int, input().split())  # read query
    print("Yes" if isLadder(arr, l-1, r) else "No")  # solve the query
