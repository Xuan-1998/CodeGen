def count_ones(n):
    total_ones = 0

    # Count ones in single-digit numbers (0-9)
    total_ones += sum(str(i).count('1') for i in range(10))

    # Count ones in two-digit numbers (10-99)
    for i in range(10, 100):
        total_ones += str(i).count('1')

    # Count ones in three-digit numbers (100-999)
    for i in range(100, 1000):
        total_ones += str(i).count('1')

    # Count ones in four-digit numbers (1000-9999)
    for i in range(1000, 10000):
        total_ones += str(i).count('1')

    # Count ones in five-digit numbers (10000-99999)
    for i in range(10000, 100000):
        total_ones += str(i).count('1')

    return total_ones

n = int(input())
print(count_ones(n))
