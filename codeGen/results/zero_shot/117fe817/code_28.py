def count_digit_ones(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += int(str(i).count('1')) + (i % 10 == 1) * (n // 10)
        else:
            count += int(str(i).count('1')) + (i % 100 >= 10 and i % 100 <= 50) * 2
    return count

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print the answer to stdout
