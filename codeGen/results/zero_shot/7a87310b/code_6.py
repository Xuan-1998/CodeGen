T = int(input())
for _ in range(T):
    N = int(input())
    count = find_positive_invertible_matrices(N)
    print(count)
