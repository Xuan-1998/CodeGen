import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    prefix_sums = [0]
    for sign in signs:
        if sign == '+':
            prefix_sums.append(prefix_sums[-1] + 1)
        else:
            prefix_sums.append(prefix_sums[-1] - 1)

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = prefix_sums[l-1]
        right_sum = prefix_sums[r]

        target_balance = (right_sum - left_sum) // 2
        if target_balance < 0:
            print(left_sum - target_balance)
        else:
            print(right_sum - target_balance)

if __name__ == '__main__':
    solve()
