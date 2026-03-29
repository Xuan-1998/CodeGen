from sys import stdin

def solve():
    n, k, m = map(int, stdin.readline().split())
    requests = [list(map(int, stdin.readline().split())) for _ in range(n)]
    requests.sort()
    
    dp = [[0] * (k + 1) for _ in range(max(m) + 1)]
    for i, (group_size, money) in enumerate(requests):
        for j in range(k, group_size - 1, -1):
            dp[group_size][j] = max(dp[group_size][j], money + dp[group_size - 1][min(j, group_size - 1)])
    
    print(dp[-1][-1])
    accepted_requests = 0
    remaining_capacity = k
    for i in range(max(m), 0, -1):
        if dp[i][remaining_capacity] > dp[i][remaining_capacity - 1]:
            print(f"{i} {remaining_capacity}")
            accepted_requests += 1
            remaining_capacity -= 1
        else:
            break

if __name__ == "__main__":
    solve()
