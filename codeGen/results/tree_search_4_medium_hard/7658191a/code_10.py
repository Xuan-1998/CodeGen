import sys

def main():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        dp = [0] * (k + 1)
        prev = [-1] * (k + 1)

        for i in range(1, k + 1):
            if i <= z:
                dp[i] = max(dp[i - 1], arr[i - 1])
            else:
                left_move = dp[i - 1] + arr[i]
                right_move = dp[i - 2] + arr[i - 1] if i > 1 else 0
                dp[i] = max(left_move, right_move)
            prev[i] = (prev[i - 1] + 1) % 2

        print(dp[k])

if __name__ == "__main__":
    main()
