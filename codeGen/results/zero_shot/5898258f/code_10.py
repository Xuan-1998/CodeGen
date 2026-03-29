def max_xor_sum(A, X):
    N = len(A)
    A.sort()
    
    # Calculate the XOR sum without adding X to any element
    xor_sum = 0
    for i in range(1, N):
        xor_sum += A[i-1] ^ A[i]
    
    # Find the maximum value by adding X to every other element
    max_xor_sum = xor_sum
    for i in range(1, N, 2):
        xor_sum += X - (A[i-1] ^ A[i])
        max_xor_sum = max(max_xor_sum, xor_sum)
    
    return max_xor_sum

# Read input from stdin and print the answer to stdout
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
