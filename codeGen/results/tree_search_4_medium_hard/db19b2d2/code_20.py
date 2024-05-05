import math

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    total_players_from_interest = sum(1 for x in s if x >= h)
    
    if total_players_from_interest < 1:
        print(-1.0)
    else:
        team_size = min(n, total_players_from_interest)
        
        p = 0
        for k in range(team_size):
            numerator = math.comb(sum(1 for x in s[:h-1] + s[h:]), k)
            denominator = math.comb(n, k)
            
            if numerator > 0 and denominator > 0:
                p += numerator / denominator
            
        print(p)

if __name__ == "__main__":
    solve()
