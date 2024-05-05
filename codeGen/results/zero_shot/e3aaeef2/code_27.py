def solve():
    t = int(input())  
    for _ in range(t):
        n, m = map(int, input().split())
        counts = [0] * 10
        while n:
            d = n % 10
            n //= 10
            counts[d] += 1
        res = sum((d+1) // 10 for d in range(9)) * m + sum(counts)
        print(res % (10**9 + 7))

solve()
