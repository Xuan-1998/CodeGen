import sys

def can_jump(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True  # We can always reach the starting point

    for i in range(1, n + 1):
        if not dp[i - 1]:  # If we cannot reach the current index
            continue
        max_reachable_index = i - 1
        for j in range(i - 1, -1, -1):  # Start from the current index and move backward
            if arr[j] >= i - j:  # The jump from this position can reach the current index
                max_reachable_index = j + arr[j]
                break
        dp[i] = (max_reachable_index >= i) or (i == n)  # If we can reach the current index, mark it as possible to reach

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_jump(arr))
