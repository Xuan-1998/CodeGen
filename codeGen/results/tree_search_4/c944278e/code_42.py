def solve(n, s):
    S = {(1 << i) - 1 for i in range(n)}
    
    for i in range(n):
        S = {team & ((1 << (n - 1)) | (1 << i)) for team in S if (s[i] == '1' and any(s[j] == '0' for j in range(i))) or (s[i] == '0' and all(s[j] == '1' for j in range(i)))}
    
    return sorted([bin(team)[2:].zfill(n) for team in S if bin(team)[2:].count('1') > 0])
