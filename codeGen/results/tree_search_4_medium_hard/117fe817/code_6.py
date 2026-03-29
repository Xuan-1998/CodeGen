def count_ones(n):
    ones = [0] * (n + 1)
    for i in range(1, n + 1):
        j = i
        while j > 0:
            if j % 10 == 1:
                ones[i] += 1
            j //= 10
    return sum(ones)

n = int(sys.stdin.readline())
print(count_ones(n))
