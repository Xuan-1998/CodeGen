def solve():
    t = int(input())  # read the number of test cases
    for _ in range(t):
        n, k = map(int, input().split())  # read n and k
        ans = 0
        for _ in range(n):
            a = int(input())  # read an array element
            if (a & ((1 << k) - 1)) > 0:  # check if the bit is set
                ans += 1
        print(ans % (10**9 + 7))

solve()
