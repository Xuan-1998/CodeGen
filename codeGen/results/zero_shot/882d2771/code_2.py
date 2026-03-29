def solve():
    t, l, r = map(int, input().split())
    f = [0] * (r + 1)
    for i in range(l, r):
        f[i + 1] = (f[i] + 2 ** (i - l + 1)) % (10**9 + 7)
    ans = t0 * f[l] + t1 * f[l + 1] + ... + tr * f[r]
    print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
