def count_digit_one(n):
    res = 0
    for i in range(1, n+1):
        # Convert integer to string to easily find number of digit '1'
        str_i = str(i)
        count_ones = str_i.count('1')
        res += count_ones
    return res

n = int(input())
print(count_digit_one(n))
