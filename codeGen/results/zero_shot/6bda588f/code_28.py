def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        f = sum((a_i - s) * (a_i - s) if a_i > s else 0 for a_i in a)
        print(f)

solve()
