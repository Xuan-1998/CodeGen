import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    memo = {}
    max_beauty = 0

    for tail_length in range(1, n + 1):
        number_of_spines = 0
        for u in range(n + 1):
            if u not in memo:
                memo[u] = (tail_length - 1, 0)
            if v := graph.get(u):
                new_tail_length, new_number_of_spines = memo[v]
                if new_tail_length > tail_length and new_tail_length <= n:
                    number_of_spines += 1
                    memo[u] = (new_tail_length, new_number_of_spines + 1)
                elif new_tail_length == tail_length:
                    number_of_spines += new_number_of_spines
            else:
                if u >= tail_length and u <= n:
                    number_of_spines += 1
        max_beauty = max(max_beauty, (tail_length * number_of_spines,))

    print(max_beauty[0] * max_beauty[1])

if __name__ == "__main__":
    solve()
