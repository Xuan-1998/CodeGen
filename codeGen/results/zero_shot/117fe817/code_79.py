def count_ones(n):
    total = 0
    for i in range(n+1):
        total += i // 10 if i < 10 else (i // 10) + (i % 10 == 1)
    return total

n = int(input())
print(count_ones(n))
