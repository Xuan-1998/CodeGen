from collections import defaultdict

def find_shortest_uncommon_subsequence():
    S, T = input().split(), input().split()
    m, n = len(S), len(T)

    # Create dictionaries to store the subsequences of each string
    S_dict, T_dict = defaultdict(int), defaultdict(int)
    for i in range(m):
        for j in range(i+1, m+1):
            S_subseq = ''.join(map(str, S[i:j]))
            S_dict[S_subseq] += 1
    for i in range(n):
        for j in range(i+1, n+1):
            T_subseq = ''.join(map(str, T[i:j]))
            T_dict[T_subseq] += 1

    # Find the minimum difference between the two dictionaries
    uncommon_subseq_len = float('inf')
    for subseq in S_dict:
        if subseq not in T_dict or S_dict[subseq] > T_dict[subseq]:
            uncommon_subseq_len = min(uncommon_subseq_len, len(subseq))

    print(uncommon_subseq_len if uncommon_subseq_len != float('inf') else -1)

find_shortest_uncommon_subsequence()
