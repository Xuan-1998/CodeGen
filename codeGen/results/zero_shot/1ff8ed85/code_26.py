def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        a = [0] * (n + 1)
        for i in range(n):
            a[i + 1] = a[i] + 1
        prefix_sum = [0]
        for i in range(1, n + 2):
            prefix_sum.append(prefix_sum[-1] + a[i - 1])
        for bi in b:
            found = False
            for i in range(n + 1):
                if prefix_sum[i] <= bi and bi < prefix_sum[i + 1]:
                    print("YES")
                    return
            print("NO")

solve()
