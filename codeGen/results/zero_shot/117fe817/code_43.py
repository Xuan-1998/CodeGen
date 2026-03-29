def count_digit_ones(n):
    count = 0
    for i in range(n + 1):
        count += str(i).count('1')
    return count

n = int(input())
print(count_digit_ones(n))
