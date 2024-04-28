import sys

def get_winning_teams(n):
    memo = {0: [0]}
    
    for i in range(1 << n):
        next_memo = {}
        for j in range(i + 1):
            if (i ^ (1 << j)) not in memo:
                memo[i ^ (1 << j)] = []
            winning_teams = memo[j] + memo[i - j - 1][::-1]
            if i == (1 << n) - 1:
                next_memo[0] = sorted(winning_teams)
            else:
                next_memo[i ^ (1 << j)] = sorted(winning_teams)
        memo.update(next_memo)
    
    return memo[(1 << n) - 1][0]

n = int(sys.stdin.readline())
print(get_winning_teams(n))
