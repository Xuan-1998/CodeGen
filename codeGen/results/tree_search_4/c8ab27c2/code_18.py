def findShortestSubArray(S: str, T: str) -> int:
    m, n = len(S), len(T)
    common_chars = set(S) & set(T)
    
    if not common_chars:
        return min(m, n)
    else:
        for i in range(len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    common_chars -= {S[i]}
                    
                if set(S[:i+1]) & common_chars and set(T[:j+1]) & common_chars:
                    return min(m, n) - (i + 1)
