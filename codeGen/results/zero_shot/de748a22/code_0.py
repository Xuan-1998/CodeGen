import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())
    sums = [0] * (n + 1)
    pos_sum, neg_sum = 0, 0
    for i in range(n):
        if signs[i] == '+':
            pos_sum += 1
        else:
            neg_sum += 1
        sums[i+1] = sums[i] + int(signs[i])

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = sums[r] - sums[l-1]
        pos_left, neg_left = 0, 0
        if l > 0:
            for i in range(l):
                if signs[i] == '+':
                    pos_left += 1
                else:
                    neg_left += 1
        right_sum = sums[r] - left_sum
        pos_right, neg_right = 0, 0
        for i in range(r, n):
            if signs[i] == '+':
                pos_right += 1
            else:
                neg_right += 1

        if (pos_left + neg_right) % 2 == 1 or (neg_left + pos_right) % 2 == 1:
            print(0)
        else:
            diff = abs(pos_left - neg_left)
            if diff > right_sum:
                print(diff)
            else:
                print(right_sum)

if __name__ == "__main__":
    solve()
