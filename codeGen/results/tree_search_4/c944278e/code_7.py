import sys

def find_winners(n):
    dp = {}
    for i in range(n+1):
        for j in range(2**n):
            if i == 0:
                dp[(i, j)] = True
            else:
                win_from_i_onwards = any((j & (1 << k)) and s[k] == '1' for k in range(i))
                dp[(i, j)] = s[i-1] == '1' or win_from_i_onwards

    winning_teams = sorted([j for i in range(n+1) for j in range(2**n) if dp[(i, j)]])
    return winning_teams

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(*find_winners(n), sep='\n')
