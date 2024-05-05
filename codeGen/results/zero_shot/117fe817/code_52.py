n = int(input())  # read input from stdin

total_count = 0
for k in range(n + 1):
    if k < 10:  # count 1's in single-digit integers
        total_count += (k == 1) + (k % 10 == 1)
    else:  # count 1's in multi-digit integers
        total_count += sum((int(digit) == 1) for digit in str(k))

print(total_count)  # print the result to stdout
