s = input().strip()
t = input().strip()

def uncommon_subsequence_length(s, t):
    s_set = set(s)
    t_set = set(t)

    uncommon_s = [i for i in s if i not in t_set]

    return -1 if len(uncommon_s) == 0 else len(uncommon_s)

print(uncommon_subsequence_length(s, t))
