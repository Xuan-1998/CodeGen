def solve():
    t, l, r = map(int, input().split())
    f_values = [0] * (r - l + 1)
    for i in range(r - l + 1):
        f_values[i] = f(l + i) % (10**9 + 7)
    
    result = sum(t_i * f_values[i] for t_i, i in enumerate(range(r - l)))
    result -= l * f(r) % (10**9 + 7)
    
    print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
