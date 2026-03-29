def count_numbers(n):
    count = 0
    for i in range(n + 1):
        if bin(i).count('0') % 2 == 1:  # check if the number has an odd number of trailing zeros
            count += 1
    return count

n = int(input())  # read input from stdin
print(count_numbers(n))  # print the result to stdout
