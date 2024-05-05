def solve(arr, x):
    n = len(arr)
    dp = [-float('inf')] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        new_xor = arr[i-1] ^ arr[i]
        for j in range(i):
            dp_val = dp[j] + new_xor
            if dp_val > max(dp[:i]) + x:
                dp[i] = dp_val
    return max(dp)

def main():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        arr = list(map(int, input().split()))
        print(solve(arr, X))

if __name__ == "__main__":
    main()
