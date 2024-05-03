from math import prod

def calculate_probability(tickets):
    n = len(tickets)
    memo = {(0, False): 1}

    def dfs(i, used_numbers, correct):
        if i == n:
            return int(correct)

        key = (used_numbers, correct)
        if key in memo:
            return memo[key]

        prob = tickets[i][0] * dfs(i + 1, tuple(x and y for x, y in zip(used_numbers, used_numbers)), correct and tickets[i][1] != tickets[i][2])
        prob += (1 - tickets[i][0]) * dfs(i + 1, tuple(x or not y for x, y in zip(used_numbers, used_numbers)), not correct)
        memo[key] = prob
        return int(prob)

    result = []
    for _ in range(int(input())):
        n = int(input())
        tickets = [list(map(int, input().split())) + [1 - p for p in map(float, input().split())] for _ in range(n)]
        result.append(str(dfs(0, (False,) * n, False)))
    print('\n'.join(result))
