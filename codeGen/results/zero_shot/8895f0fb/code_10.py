T = int(input())
for _ in range(T):
    N = int(input())
    total_carries = 0
    for i in range(10**N):
        A = str(i).zfill(N)
        for j in range(i+1, 10**N):
            B = str(j).zfill(N)
            carries = sum((int(a) + int(b)) >= 10 for a, b in zip(A, B))
            total_carries += carries
    print(total_carries / (9*10**(2*N-1)))
