def can_partition(A):
    N = len(A)
    A.sort()
    K, M = map(int, input().split())
    
    for i in range(N-K+1):
        if A[i+K-1] - A[i] > M:
            return False
    
    return True

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(can_partition(A))
