import sys

def solve():
    n, q = map(int, input().split())
    sign_list = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        sign_sum = 0
        cum_sum = 0
        remove_count = 0
        for i in range(l-1, r):
            sign_sum += int(sign_list[i])
            if sign_sum > 0:
                cum_sum += 1
            elif sign_sum < 0:
                cum_sum -= 1
            if cum_sum == 0:
                remove_count = max(0, remove_count-1)
        print(remove_count)

if __name__ == "__main__":
    solve()
