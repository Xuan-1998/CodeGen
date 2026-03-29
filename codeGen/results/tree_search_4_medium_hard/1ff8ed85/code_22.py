def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        a = [0]
        for i in range(n-1):
            if b[i] > b[i+1]:
                a.append(b[i])
            else:
                a[-1] += 1
        a.append(b[-1])
        print("YES" if a == list(map(len, [str(i) for i in b])) else "NO")

solve()
