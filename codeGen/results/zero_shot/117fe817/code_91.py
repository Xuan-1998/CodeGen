import sys

n = int(sys.stdin.read())

count_no_ones = n // 10
count_with_one = (n - 1) // 9

total_count = count_no_ones * 9 + count_with_one
print(total_count)
