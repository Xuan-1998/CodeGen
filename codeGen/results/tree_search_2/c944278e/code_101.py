from collections import defaultdict

def find_winners(n, s):
    memo = defaultdict(list)
    max_phase = 2**n - 1

    def dfs(phase):
        if phase == max_phase:
            return [s[:], ]
        if (phase,) in memo:
            return memo[phase]
        winners = []
        for i in range(2**n):
            if ((i >> phase) & 1) == int(s[phase]):
                winners.extend(dfs(phase + 1))
        memo[(phase,)] = winners
        return winners

    return sorted(set([s[:]] + ["".join(winner[::-1]) for winner in dfs(0)]))

n = int(input())
s = input()
print(find_winners(n, s))
