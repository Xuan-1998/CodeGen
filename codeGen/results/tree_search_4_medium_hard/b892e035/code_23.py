from collections import defaultdict

def calculate_probability():
    T = int(input())
    memo = defaultdict(float)

    def prob(n):
        if n in memo:
            return memo[n]
        
        if n == 1:
            p = 1.0
            for _ in range(2):
                a, b, p_i = map(int, input().split())
                p *= p_i / (1 - p_i)
            return p
        
        p_total = 0.0
        for a, b, p_a, p_b in [map(int, line.split()) for line in [input() for _ in range(n)]]:
            if a not in memo:
                memo[a] = prob(a)
            if b not in memo:
                memo[b] = prob(b)
            
            p_total += (p_a * p_memo_a + p_b * p_memo_b) / 2.0
        return p_total

    for _ in range(T):
        n = int(input())
        print(prob(n))
