def solve():
    n = int(input())
    m = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if m[i] < m[i-1]:
            count += 1
    print(count % (10**9 + 7))

solve()
