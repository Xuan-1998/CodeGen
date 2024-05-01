def find_winning_teams(n):
    win = [False] * (1 << n)
    
    for i in range(len(s)):
        bit = int((1 << i) & s[-1 -i])
        if bit:
            for j in range(1 << n):
                if not win[j]:
                    win[j | bit] = True
        else:
            for j in range(1 << n):
                if win[j]:
                    win[j ^ (1 << i)] = True
    
    winning_teams = [j for j in range(1 << n) if win[j]]
    return sorted(winning_teams)
