def uncommonFromS(T):
    S = input()
    s_len = len(S)
    t_len = len(T)

    res = -1
    for i in range(1 << (s_len + 1)):
        subseq = ''
        for j in range(s_len):
            if ((i & (1 << j)) > 0) and S[j] not in subseq:
                subseq += S[j]
        
        if len(subseq) <= t_len:
            if all(x not in T for x in subseq):
                res = max(res, len(subseq))
    
    print(res)
