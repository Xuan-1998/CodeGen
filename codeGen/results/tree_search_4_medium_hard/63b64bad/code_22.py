from collections import defaultdict

def solve_sequence():
    n = int(input())
    sequence = list(map(int, input().split()))

    memo = defaultdict(lambda: -1)

    def state_transition(state):
        x, y = state
        if x <= 0 or x > n:
            return -1
        new_x = (x + sequence[x] - 1) % n
        if new_x == x:
            return state
        new_y = y + sequence[x]
        return (new_x, new_y)

    def dfs(state):
        if memo[state] != -1:
            return memo[state]
        result = state_transition(state)
        if result != -1:
            memo[state] = result
            return dfs(result)
        else:
            return result

    final_results = []
    for i in range(2, n + 1):
        result = dfs((i, 0))
        if result == -1:
            final_results.append(-1)
        else:
            final_results.append(result[1])

    print('\n'.join(map(str, final_results)))

if __name__ == "__main__":
    solve_sequence()
