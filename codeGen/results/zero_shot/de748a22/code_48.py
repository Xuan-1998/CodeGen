def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        sign_sum = sum(signs[l-1:r])
        if sign_sum == 0:
            print(0)
        else:
            if sign_sum > 0:
                print(r-l+1)
            else:
                print(-sign_sum)

if __name__ == "__main__":
    solve()
