from collections import defaultdict

def is_ladder(arr):
    dp = defaultdict(bool)
    max_length = 0
    for i in range(len(arr)):
        if i == 0 or arr[i] >= arr[i-1]:
            if i > 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = True
            max_length = i+1
        else:
            dp[i] = False
    return dp

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = is_ladder(arr)
    for _ in range(m):
        l, r = map(int, input().split())
        if dp[r]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()
