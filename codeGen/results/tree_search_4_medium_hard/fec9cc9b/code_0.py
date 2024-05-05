def is_ladder(arr):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if arr[j] >= arr[j - 1]:
                dp[i][j] = True
            else:
                for k in range(j - 1, i - 1, -1):
                    if dp[i][k] and arr[k] <= arr[k + 1]:
                        dp[i][j] = True
                        break
    
    return dp[0][n - 1]


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(m):
        l, r = map(int, input().split())
        if is_ladder(arr[l - 1:r]):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
