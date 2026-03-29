import sys

def query_sum(arr, l, r):
    return sum(arr[i] if i < l else -arr[i] for i in range(r-l+1))

def min_remove_sign_var_sum(arr, l, r):
    n = len(arr)
    prefix_sum = [0]
    sign_sum = 0
    for a in arr:
        sign_sum += a
        prefix_sum.append(prefix_sum[-1] + sign_sum)

    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = abs(arr[i-1])
        for j in range(i-1, -1, -1):
            if arr[j-1]*arr[i-1] > 0:
                dp[i][j] = min(dp[i-1][j-1]+abs(arr[i-1]), dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return min(dp[r][l], key=lambda x: x+query_sum(arr, l, r))

def main():
    n, q = map(int, input().split())
    arr = list(input())
    for _ in range(q):
        l, r = map(lambda x: int(x)-1, input().split())
        print(min_remove_sign_var_sum([1 if a == '+' else -1 for a in arr], l, r))

if __name__ == "__main__":
    main()
