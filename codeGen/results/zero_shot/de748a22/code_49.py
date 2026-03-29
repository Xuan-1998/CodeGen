def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = sum(signs[l-1:r])
        right_sum = -left_sum

        print(min(r-l+1, abs(left_sum-right_sum)))

if __name__ == '__main__':
    solve()
