import sys

def count_digit_ones(n):
    def f(k):
        if k == 0:
            return 0
        else:
            return 1 + (k > 9 and f(k-2)) or 0

    total_count = 0
    for i in range(n+1):
        total_count += f(i)
    return total_count

n = int(sys.stdin.readline())
print(count_digit_ones(n))
