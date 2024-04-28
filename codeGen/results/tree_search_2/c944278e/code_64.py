from collections import defaultdict

def dp(s):
    n = len(s)
    if n == 1:  # Base case: single team wins
        return [0]

    memo = defaultdict(list)

    def dfs(i):
        if i >= n:
            return [i]
        if (i, s[:i]) in memo:
            return memo[(i, s[:i])]
        res = []
        for j in range(2**n):
            if bin(j)[2:].zfill(n)[:i] == s[:i]:
                if (j ^ 1) > i:  # If the right child wins
                    res += dfs(i+1)
                else:  # If the left child wins
                    res.append(i)
        memo[(i, s[:i])] = res
        return res

    return [x for x in dfs(0) if bin(2**n - 1)[2:].zfill(n)[:x] == '1' * (n-1)]

def main():
    n = int(input())
    s = input()
    winning_teams = dp(s)
    print(*winning_teams, sep='\n')

if __name__ == "__main__":
    main()
