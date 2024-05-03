from collections import defaultdict

def can_make_zero(n, arr):
    dp = defaultdict(bool)
    dp[(-1, -1)] = True  # Base case: empty array is always possible to make zero

    for i in range(n):
        left_sum = sum(arr[:i+1])
        right_sum = sum(arr[i:])
        if dp[(left_sum, right_sum)]:
            return "YES"
        dp[(left_sum, right_sum)] = False
    return "NO"

n = int(input())
for _ in range(n):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_make_zero(n, arr))
