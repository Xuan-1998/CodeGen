def find_count(n):
    total = 0
    for i in range(0, len(str(n))):
        total += (n // 10**i) % 10
    return total

n = int(input())
print(find_count(n))
