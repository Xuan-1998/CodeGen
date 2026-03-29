def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        sign_sum = sum(1 if signs[i] == '+' else -1 for i in range(l-1, r))
        if sign_sum % 2 != 0:
            print(min(r-l+1, abs(sign_sum)//2))
        else:
            print(0)

if __name__ == "__main__":
    solve()
