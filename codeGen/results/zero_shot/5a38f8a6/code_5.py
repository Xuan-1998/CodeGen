def num_squares(n):
    count = 0
    while n > 0:
        i = int(n ** 0.5)
        if i * i == n:
            return count + 1
        n -= i * i
        count += 1
    return count

n = int(input())
print(num_squares(n))
