from collections import defaultdict

def count_blocks(n):
    res = [0] * (n + 1)
    for i in range(10**n, -1, -1):
        s = str(i).zfill(n)
        for j in range(len(s)):
            if j == 0 or s[j] != s[0]:
                break
            res[len(str(j+1))] += 1
    return [x % 998244353 for x in res]
