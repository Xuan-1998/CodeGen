def count_digit1(n):
    def count OnesInNumber(x):
        return bin(x).count('1')

    total_ones = 0
    for i in range(n + 1):
        total_ones += OnesInNumber(i)
    return total_ones

n = int(input())
print(count_digit1(n))
