from collections import defaultdict

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = defaultdict(lambda: float('inf'))
    dp[(0, "")] = 0

    for i in range(1, n + 1):
        for j in range(i):
            s = "".join(sorted(strings[j], reverse=costs[j] % 2 == 1))
            t_cost = dp[(j, s)]
            if t_cost != float('inf'):
                dp[(i, s)] = min(dp[(i, s)], t_cost)
        for j in range(i):
            s = strings[j][::-1]
            t_cost = dp[(j, s)]
            if t_cost != float('inf'):
                dp[(i, s)] = min(dp[(i, s)], t_cost + costs[i])

    res = min(dp.values(), default=-1)
    print(res)

if __name__ == "__main__":
    solve()
