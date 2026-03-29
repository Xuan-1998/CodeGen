def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        total_signs = sum(signs[l-1:r])
        if total_signs == 0:
            print(0)
        else:
            print(abs(total_signs))

if __name__ == "__main__":
    solve()
