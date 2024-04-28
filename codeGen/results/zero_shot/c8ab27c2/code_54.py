s = input().strip()
t = input().strip()

def uncommon_subsequence(s, t):
    s_set = set(s)
    t_set = set(t)

    uncommon_len = 0
    for char in s_set:
        if char not in t_set and len([c for c in s if c == char]) > uncommon_len:
            uncommon_len = len([c for c in s if c == char])

    return -1 if uncommon_len == 0 else uncommon_len

print(uncommon_subsequence(s, t))
