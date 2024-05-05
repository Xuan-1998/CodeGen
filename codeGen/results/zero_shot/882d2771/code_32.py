def solve():
    t, l, r = map(int, input().split())
    f_values = [0] * (r - l + 1)
    # calculate f_values...
    result = sum(t[i] * f_values[i - l] for i in range(l, r+1)) % (10**9 + 7)
    print(result)

if __name__ == "__main__":
    solve()
