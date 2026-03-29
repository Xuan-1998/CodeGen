import sys

def count_digit_ones(n):
    count = 0
    for k in range(10):  # iterate over each digit place (ones, tens, hundreds, etc.)
        count += min(n // 10**k, (1 << (k+1)) - 1)  # calculate the count of 1's in this digit place
    return count

n = int(sys.stdin.readline())
print(count_digit_ones(n))
