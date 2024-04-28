def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [0] * (n + 1)
        total_sum = sum(arr)
        left_sum = 0
        res = 0
        for i in range(n):
            if left_sum == total_sum - left_sum:
                res += 1
                left_sum = 0
            else:
                j = i
                while j > 0 and arr[j-1] <= arr[i]:
                    j -= 1
                dp[i+1] = max(dp[i], dp[j]+(left_sum == total_sum - left_sum))
                left_sum += arr[i]
        print(res + (dp[-1] > res))

if __name__ == "__main__":
    solve()
