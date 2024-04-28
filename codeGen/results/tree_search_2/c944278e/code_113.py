import sys

def find_winners(n, s):
    MOD = 10**9 + 7
    dp = {(i, [1 << i for _ in range(n)]) : [0] for i in range(2**n)}
    
    for curr_level in range(n-1, -1, -1):
        for mask in range(2**curr_level):
            remaining_teams = [i+1 for i in range(curr_level) if (mask >> i) & 1]
            winner = s[curr_level-1] == '0' and 2**(n-1-curr_level) or 2**(n-1-curr_level)-1
            dp[(curr_level, remaining_teams)] = [i for i in dp[(curr_level+1, remaining_teams + [winner])]
    
    return sorted([team for teams in dp.values() for team in teams])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    print(find_winners(n, s))
