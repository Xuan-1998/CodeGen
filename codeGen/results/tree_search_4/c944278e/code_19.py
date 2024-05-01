import sys

def winning_teams(n):
    s = [int(x) for x in input().split()]
    
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return True
        
        if s[i-1] == 0:  # team j lost
            memo[(i, j)] = False
            return False
        
        for k in range(2**n):
            if dp(i-1, k) and (k & (1 << (j - 1))) == 0:
                memo[(i, j)] = True
                return True
        
        memo[(i, j)] = False
        return False

    winning_teams = []

    for j in range(2**n):
        if dp(n, j):
            winning_teams.append(j)

    print(' '.join(map(str, sorted(winning_teams))))


if __name__ == '__main__':
    n = int(input())
    winning_teams(n)
