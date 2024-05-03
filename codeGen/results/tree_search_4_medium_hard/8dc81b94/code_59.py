import sys

def can_zero_out(arr):
    n = len(arr)
    dp = [False] * (n + 1)

    dp[0] = True
    for i in range(1, n + 1):
        if arr[i - 1] == 0:
            dp[i] = dp[i - 1]
        else:
            left_diff = right_diff = sys.maxsize
            j = k = 0
            while j < i and k > 0:
                if abs(arr[j] - arr[k]) <= min(left_diff, right_diff):
                    left_diff = right_diff = abs(arr[j] - arr[k])
                    j += 1
                    k -= 1
                elif arr[j] < arr[k]:
                    j += 1
                else:
                    k -= 1
            if left_diff == sys.maxsize and right_diff == sys.maxsize:
                dp[i] = True

    return "YES" if any(dp) else "NO"

# Input: Read from standard input
n = int(input())
arr = list(map(int, input().split()))

print(can_zero_out(arr))
