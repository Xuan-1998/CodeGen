import sys

def solve():
    n, q = map(int, input().split())
    signs = list(map(lambda x: 1 if x == "+" else -1, input()))

    prefix_sum = [0]
    for sign in signs:
        prefix_sum.append(prefix_sum[-1] + sign)

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = prefix_sum[l-1]
        right_sum = prefix_sum[r]

        if (right_sum - left_sum) % 2 == 0:
            print(0)
        else:
            print(min(r-l+1, (prefix_sum[r] - left_sum) // 2))

if __name__ == "__main__":
    solve()
