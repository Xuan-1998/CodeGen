from collections import deque, defaultdict

def simulate_sequence(a):
    n = len(a) + 1
    graph = defaultdict(list)
    memo = {}

    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        if x <= 0 or x > n:
            return y
        graph[(x, y)].extend([(x+a[x], y+a[x]), (max(1, x-a[x]), y+a[x])])
        return max(dfs(x+a[x], y+a[x]), dfs(max(1, x-a[x]), y+a[x]))

    for i in range(n):
        print(dfs(1, 0))

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    simulate_sequence(a)
