def solve(n, a):
    mod = 10**9 + 7
    ans = 0

    for i in range(1, n+1):
        cnt_A = sum(j % i == 0 for j in range(i, a[i-1]+1))
        if a[i-1] % i == 0:
            ans += (cnt_A + 1) * (a[i-1] // i)
        else:
            ans += cnt_A

    return ans % mod
