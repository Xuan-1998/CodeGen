s = input().strip()
t = input().strip()

def uncommon_subsequence(s, t):
    s_set = set([s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)])
    t_set = set([t[i:j] for i in range(len(t)) for j in range(i+1, len(t)+1)])

    uncommon = [subsequence for subsequence in s_set if subsequence not in t_set]

    return min(len(sub) for sub in uncommon) if uncommon else -1

print(uncommon_subsequence(s, t))
