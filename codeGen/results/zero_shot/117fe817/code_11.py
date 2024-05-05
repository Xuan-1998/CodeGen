def count_digit_ones(n):
    ones_count = 0
    for i in range(10**n.bit_length()):
        num = i * 2 + 1  # tricky part: only consider numbers with digit 1
        ones_count += sum(int(digit) == 1 for digit in str(num))
    return ones_count

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print the result to stdout
