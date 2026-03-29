from sys import stdin

def can_reach_last_index(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        if arr[i - 1] >= i:
            j = min(i - 1, i - arr[i - 1])
            while j >= 0 and not dp[j]:
                j -= 1
            if j < 0 or dp[j]:
                dp[i] = True
        else:
            break

    return dp[-1]

if __name__ == "__main__":
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    print(can_reach_last_index(arr))
