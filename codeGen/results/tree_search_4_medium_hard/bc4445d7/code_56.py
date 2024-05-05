import sys

def solve():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        edges = list(map(lambda x: [int(x) for x in x.split()], [input().split() for _ in range(n-1)]))
        m = int(input())
        primes = list(map(int, input().split()))
        memo = {}

        def dfs(node):
            if node not in memo:
                memo[node] = 0
                for neighbor, label in edges[node]:
                    if label != 1:
                        memo[node] += dfs(neighbor) * label
                    else:
                        memo[node] += 1
            return memo[node]

        total_distribution_index = 0
        for i in range(n):
            total_distribution_index += dfs(i)
        print(total_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
