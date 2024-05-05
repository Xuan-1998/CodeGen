from collections import defaultdict

def is_possible_to_partition(A):
    N, K, M = A[0], A[1], A[2]
    A = A[3:]
    
    memo = {}
    dp = defaultdict(bool)
    
    for i in range(N+1):
        for j in range(K+1):
            if j == 0:
                dp[(i, j)] = True
            else:
                if (i-1, j) not in dp and ((i==0 or abs(A[i-1]-A[i])<=M) or (i>0 and dp[(i-1, j-1)])):
                    dp[(i, j)] = True
                else:
                    dp[(i, j)] = False
    
    return dp[(N, K)]

# Example usage:
input_data = [int(x) for x in input().split()]
print(is_possible_to_partition(input_data))
