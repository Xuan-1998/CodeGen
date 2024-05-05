from collections import defaultdict

def main():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    memo = {(i, p): float('inf') for i in range(2, n + 1) for p in range(n)}

    def dfs(city, roads_inverted):
        if memo[city][roads_inverted] != float('inf'):
            return memo[city][roads_inverted]
        if city == 1:
            return roads_inverted
        result = float('inf')
        for neighbor in graph[city]:
            result = min(result, dfs(neighbor, roads_inverted + 1))
        memo[city][roads_inversed] = result + 1
        return result

    cities_to_capital = list(range(2, n + 1))
    capital = min((city for city in cities_to_capital), key=lambda x: dfs(x, 0))

    roads_to_reverse = dfs(capital, 0)
    print(roads_to_reverse)

    ways_to_choose_capital = [(i,) for i in range(2, n + 1)]
    ways_to_choose_capital.sort(key=lambda x: x[0])
    print(*ways_to_choose_capital[0], sep=' ')

if __name__ == '__main__':
    main()
