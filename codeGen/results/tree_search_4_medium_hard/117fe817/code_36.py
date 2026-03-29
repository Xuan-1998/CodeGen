def count_ones(n):
    Memo = {}
    def dp(k, n):
        if (k, n) in Memo: return Memo[(k, n)]
        if n < 10**(k-1): return 0
        result = sum(dp(k-1, int(str(n)[:i+1])) for i in range(min(len(str(n)), k))) + (str(n)[k] == '1')
        Memo[(k, n)] = result
        return result

    return dp(len(str(n)), n)
