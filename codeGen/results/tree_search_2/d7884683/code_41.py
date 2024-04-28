from sys import stdin, stdout

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        dp = [0] * (n + 1)
        dp[0] = 0
        max_partitions = 0
        for i in range(1, n + 1):
            left_sum = sum(arr[:i])
            j = i - 1
            while j >= 0 and left_sum == sum(arr[j:i]):
                max_partitions = max(max_partitions, dp[j] + 1)
                j -= 1
            dp[i] = max_partition
        stdout.write(str(max_partitions) + '\n')

if __name__ == '__main__':
    solve()
