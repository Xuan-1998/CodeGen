def count_matrices(n):
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for d in range(b, n+1):
                c = (a*d - n) // (d-b)
                if c >= b and (a*d - b*c) > 0:
                    count += 1
    return count

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_matrices(n))
