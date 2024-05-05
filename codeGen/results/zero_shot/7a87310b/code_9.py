def count_positive_invertible_matrices(n):
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            for k in range(j, n+1):
                if (i + k) == n and ((k - i) > 0 or (j - k) > 0):
                    count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_positive_invertible_matrices(n))
