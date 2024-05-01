def uncommon_subsequences(S, T):
    memo = {}

    def dfs(i1, i2):
        if (i1, i2) not in memo:
            if i1 == len(S) and i2 == len(T):
                return 0
            elif i1 >= len(S) or i2 >= len(T):
                return float('inf')
            else:
                c1, c2 = S[i1], T[i2]
                if c1 != c2:
                    return dfs(i1 + 1, i2)
                else:
                    memo[(i1, i2)] = dfs(i1 + 1, i2) + 1
        return memo[(i1, i2)]

    return dfs(0, 0)

# Read input from standard input
S, T = input().split()

# Print the answer to standard output
print(uncommon_subsequences(S, T))
