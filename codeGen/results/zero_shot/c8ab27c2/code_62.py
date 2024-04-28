s = input()
t = input()

def uncommon_subsequences(s, t):
    s_len, t_len = len(s), len(t)
    res = float('inf')
    
    for i in range(s_len - t_len + 1):
        common = False
        for j in range(t_len):
            if s[i+j] != t[j]:
                break
        else:
            common = True
        
        if not common:
            res = min(res, s_len - (i + t_len))

    return -1 if res == float('inf') else res

print(uncommon_subsequences(s, t))
