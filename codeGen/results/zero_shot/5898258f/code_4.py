T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    result = 0
    for i in range(1, N):
        result += A[i-1] ^ A[i]
    
    max_xor = 0
    for i in range(N):
        xor_sum = 0
        for j in range(i, N):
            xor_sum += A[j]
            if xor_sum > X:
                break
            else:
                max_xor = max(max_xor, xor_sum ^ X)
    
    print(result + max_xor)
