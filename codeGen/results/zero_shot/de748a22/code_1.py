def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = sum(signs[:l])
        right_sum = sum(signs[r:])

        if left_sum == right_sum:
            print(0)
        else:
            if left_sum > right_sum:
                print(r - l + 1)
            else:
                print(l - r - 1)

if __name__ == "__main__":
    solve()
