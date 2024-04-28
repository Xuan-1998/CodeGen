s = input().strip()
t = input().strip()

def uncommon_subsequence_length(s, t):
    s_set = set([s[i:i+1] for i in range(len(s))])
    t_set = set([t[i:i+1] for i in range(len(t))])

    common_chars = s_set & t_set
    uncommon_chars = s_set - common_chars

    return len(uncommon_chars) if uncommon_chars else -1

print(uncommon_subsequence_length(s, t))
