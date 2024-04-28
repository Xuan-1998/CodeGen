import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = {(0, 0): 1}
        total_sum = sum(arr)
        for i in range(1, n+1):
            left_sum = total_sum - sum(arr[i:])
            if (i-1, left_sum) not in dp:
                dp[(i, left_sum)] = 0
            if (i-1, left_sum+arr[0]) not in dp:
                dp[(i, left_sum+arr[0])] = 0
            dp[(i, left_sum)] = max(dp.get((i-1, left_sum-arr[i]), 0) + dp.get((i-1, left_sum+arr[0]), 0), 1)
        print(max(dp.values()))

solve()
