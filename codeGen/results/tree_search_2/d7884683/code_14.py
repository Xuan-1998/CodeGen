def partition_equal_sum(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        if arr[i - 1] % 2 == 0:
            for j in range(i - 1, -1, -1):
                if dp[j]:
                    dp[i] = (sum(arr[:j]) == sum(arr[i - j:]))
                    break
    return max((i for i in range(len(dp) - 1) if dp[i])) + 1 if any(dp) else 0

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(partition_equal_sum(arr))

if __name__ == "__main__":
    main()
