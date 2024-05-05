def solve(t, l, r):
    # TO DO: implement function f(n) here!
    pass

if __name__ == "__main__":
    t, l, r = map(int, input().split())
    result = solve(t, l, r)
    print(result % (10**9 + 7))
