import heapq

n = int(input())  # read n
a, b, c = [list(map(int, input().split())) for _ in range(3)]  # read all three lines of integers

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = [c[i], c[i]]

# fill up the dynamic programming table
for length in range(2, n+1):
    for start in range(n-length+1):
        end = start + length - 1
        if start == 0:
            dp[start][end] = [a[0], a[0]]
        elif end == n-1:
            dp[start][end] = [c[end], c[end]]
        else:
            # consider the last hop: whether it's fed or not
            for mid in range(start, end+1):
                if mid == start:
                    # first hop: only one adjacent full hare
                    dp[start][end] = [max(dp[start][mid-1][0], a[mid]), max(dp[start][mid-1][1], b[mid])]
                else:
                    # middle hops
                    dp[start][end] = [max(max(dp[start][mid-1][0], a[mid]), dp[mid][end][0]), 
                                       max(max(dp[start][mid-1][1], b[mid]), dp[mid][end][1])]
            if start == 0:
                # first hop: only one adjacent full hare
                dp[start][end] = [max(dp[0][end][0], c[end]), max(dp[0][end][1], c[end])]
            elif end == n-1:
                # last hop: both adjacent hares are full
                dp[start][end] = [c[0], c[0]]

# the maximum total joy is in the bottom-right corner of the table
print(max(max(dp)))
