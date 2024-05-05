def count_matrices(n):
    count = 0
    for i in range(1, n//2 + 1):
        d = (n-1)//2 * (n+1)//2 - i*(n-i)
        if d > 0:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_matrices(n))
