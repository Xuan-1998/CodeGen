def max_points(n):
    memo = {}
    def dp(i):
        if i in memo:
            return memo[i]
        if i == n:  # base case: when all elements have been processed
            return 0
        if not dp(i+1):  # if the current sequence is empty
            return float('inf')  # return infinity, since we can't earn points

        max_points = 0
        for k in range(1, n+1):
            if i+k <= n and a[i+k-1] - a[i-1] == k:
                # if the current sequence is complete, delete it and recursively call dp on the remaining elements
                res = 1 + dp(i+k)
                max_points = max(max_points, res)
        memo[i] = max_points
        return max_points

    a = list(map(int, input().split()))  # read in the sequence
    n = len(a)  # get the number of elements in the sequence
    print(dp(1))  # start with the first element and recursively call dp on the remaining elements


# receive inputs from stdin and print answer to stdout
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    output = sys.stdout.write
    n = int(input())
    a = list(map(int, input().split()))
    print(max_points(n))
