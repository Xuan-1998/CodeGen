def solve():
    n = int(input())
    p = list(map(int, input().split()))
    a, b = [], []
    for i in range(n):
        if p[i] < p[n+i]:
            a.append(p[i])
        else:
            b.append(p[i])
    if len(a) + len(b) == 2*n and set(a).isdisjoint(set(b)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
