def find_winning_teams(n, s):
    memo = {}

    def dfs(i, mask):
        if (i, mask) in memo:
            return memo[(i, mask)]
        if i == 0:
            return [0] if int(s[:i].replace('1', '0').replace('0', '1'), 2) < int(s, 2) else [int(s[:i], 2)]

        winning_teams = []
        for j in range(2**n):
            if (j >> i) & 1:
                opposite_team = ~j
                opposite_mask = mask ^ (1 << i)
                opposite_result = dfs(i-1, opposite_mask)

                if len(opposite_result) > 0 and int(s[i-1], 2) == 1:
                    winning_teams.extend([i] + t for t in opposite_result)
            else:
                opposite_team = j
                opposite_mask = mask & ~(1 << i)
                opposite_result = dfs(i-1, opposite_mask)

                if len(opposite_result) > 0 and int(s[i-1], 2) == 0:
                    winning_teams.extend([i] + t for t in opposite_result)
        return sorted(set(winning_teams))

    return dfs(n-1, (1 << n) - 1)


# Example usage
n = int(input())
s = input()
print(*find_winning_teams(n, s), sep='\n')
