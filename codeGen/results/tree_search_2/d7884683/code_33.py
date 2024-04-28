from sys import stdin

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            left_sum = sum(arr[:i])
            for j in range(i):
                right_sum = sum(arr[i:])
                if left_sum == right_sum:
                    dp[i][j] += 1
        print(max(max(row) for row in dp))

if __name__ == "__main__":
    solve()
