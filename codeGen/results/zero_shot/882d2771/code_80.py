def f(n, memo={}):
    if n <= 1:
        return 0
    if n not in memo:
        memo[n] = min((k * f(k, memo) + (n - k) * f(n - k, memo)) % (10**9 + 7) for k in range(1, n+1))
    return memo[n]

def main():
    t, l, r = map(int, input().split())
    print(f(t) * f(l-1) * f(r-1) % (10**9 + 7))

if __name__ == "__main__":
    main()
