from collections import defaultdict

def solve():
    n = int(input())
    t = input()
    s = [input() for _ in range(n)]
    
    dp = defaultdict(lambda: -1)
    res = 0
    
    for i in range(len(t) - 1, -1, -1):
        colored = set()
        for j in range(i + len(s[0])):
            if all(t[k] == s[i][k % len(s[0])][j % len(s[0])) for k in range(j)):
                colored.add(j)
        
        if not colored:
            return -1
        
        dp[(i, tuple(sorted(colored)))] = 1 + sum(dp.get((k, tuple(sorted(colored & set(range(k))))), float('inf')) for k in sorted(colored))
    
    res = min(sum(dp.get((t.index(c) or len(t), set()), float('inf')) for c in s[0]), len(t))
    
    if res == -1:
        return -1
    else:
        w_j, p_j = [], []
        colored = set()
        for i in range(len(t)):
            if i not in colored and t[i] != s[0][i % len(s[0])]:
                j = dp.get((i, tuple(sorted(colored | {i}))), float('inf'))
                w_j.append(0)
                p_j.append(i)
                res -= 1
                colored.add(i)
        
        return str(res) + '\n' + '\n'.join(f'{w_j[j]} {p_j[j]}' for j in range(len(w_j)))

print(solve())
