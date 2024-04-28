s = input().strip()
t = input().strip()

def uncommon_subsequence_length():
    s_set = set([s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)])
    t_set = set([t[i:j] for i in range(len(t)) for j in range(i+1, len(t)+1)])

    uncommon = s_set - t_set
    return min(len(sub) if sub in s_set else float('inf') for sub in uncommon) if uncommon else -1

print(uncommon_subsequence_length())
