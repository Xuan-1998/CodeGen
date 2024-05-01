def solve(n):
    memo = {}
    def dfs(mask, state):
        if (mask,) in memo:
            return memo[(mask,)]
        if bin(int(bin(state)[2:], 2)).count('1') == 1:
            return [(state,)]
        res = []
        for i in range(n):
            if not ((1 << i) & mask):
                next_state = state | (1 << i)
                res.extend(dfs(mask ^ (1 << i), next_state))
        memo[(mask,)] = res
        return res

    def get_winners(mask):
        winners = []
        for skill in range(2**n):
            if all(((skill >> i) & 1) <= ((s >> i) & 1) for s in dfs(mask, skill)[0]):
                winners.append(bin(skill)[2:].zfill(n))
        return sorted(winners)

    return '\n'.join(get_winners((1 << n) - 1))

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
