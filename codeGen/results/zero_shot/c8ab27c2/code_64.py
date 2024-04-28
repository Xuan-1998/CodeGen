s = input().strip()
t = input().strip()

def uncommon_subsequence_length(s, t):
    s_set = set([s[i:j+1] for i in range(len(s)) for j in range(i+len(s)-i)])
    common = s_set & set([t[i:j+1] for i in range(len(t)) for j in range(i+len(t)-i)])
    uncommon = s_set - common
    return len(uncommon) if uncommon else -1

print(uncommon_subsequence_length(s, t))
