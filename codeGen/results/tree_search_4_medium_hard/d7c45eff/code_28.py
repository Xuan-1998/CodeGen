import sys

def transition(s):
    if len(s) > 0:
        return [s[:-1], s + s]
    else:
        return [""]

def answer(n, k):
    current_state = [s for _ in range(len(s))]
    min_str = ""

    dp = {}
    def dfs(state, left):
        if (state, left) in dp:
            return dp[(state, left)]
        if left == 0:
            dp[(state, left)] = state
            return state
        result = ""
        for i in range(len(state)):
            if i + left <= k and len(state) - i >= left:
                new_state = state[i:]
                if new_state < state:
                    result = min(result, dfs(new_state[::-1], left-1))
            elif i + 2 * (len(state) - i) <= k:
                new_state = state[i:] + state[:i]
                if new_state < state:
                    result = min(result, dfs(new_state[::-1], left-1))
        dp[(state, left)] = result
        return result

    for i in range(k):
        next_states = transition(current_state)
        current_state = [s for s in next_states]
    min_str = dfs(s, k)
    return min_str

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
print(answer(n, k))
