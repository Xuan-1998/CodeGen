def tournament_winner(n):
    def dfs(phase, states, memo):
        if phase >= n:
            return [states[0]]
        winners = []
        for i in range(2**n):
            state = states.copy()
            for j in range(n):
                if (i >> j) & 1:
                    state[j] += 1
            if dfs(phase+1, state, memo).count(True):
                winners.append(state[0])
        return [winners]

    def solve():
        n = int(input())
        s = input()
        memo = {}
        return '\n'.join(map(str, sorted(set([dfs(0, [0]*n, memo)[0] for _ in range(n)]))))

    print(solve())
