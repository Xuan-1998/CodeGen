from collections import defaultdict

def solve():
    n, m, c0, d0 = map(int, input().split())
    ai = [int(x) for x in input().split()]
    bi = [int(x) for x in input().split()]
    ci = [int(x) for x in input().split()]
    di = [int(x) for x in input().split()]

    memo = defaultdict(int)

    def dfs(stuffing_type, remaining_dough):
        if (stuffing_type, remaining_dough) in memo:
            return memo[(stuffing_type, remaining_dough)]

        if stuffing_type == m or remaining_dough == 0:
            return 0

        max_profit = 0
        if ai[stuffing_type] > 0 and remaining_dough >= bi[stuffing_type] + ci[stuffing_type]:
            profit_with_stuffing = di[stuffing_type] - bi[stuffing_type] - ci[stuffing_type]
            max_profit = max(max_profit, dfs(stuffing_type + 1, remaining_dough - (bi[stuffing_type] + ci[stuffing_type])) + profit_with_stuffing)
        else:
            max_profit = dfs(stuffing_type + 1, remaining_dough)

        memo[(stuffing_type, remaining_dough)] = max_profit
        return max_profit

    print(dfs(0, c0))

if __name__ == "__main__":
    solve()
