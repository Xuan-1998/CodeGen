import sys

def min_falling_path_sum(A):
    memo = {(0, j): A[0][j] for j in range(len(A[0]))}
    
    for i in range(1, len(A)):
        memo[(i, 0)] = max(memo[(i-1, k)] + A[i][k] for k in range(len(A[0])))
        
        for j in range(1, len(A[0])):
            memo[(i, j)] = min(memo[(i-1, k-1)]*A[0][k] for k in range(j)) + A[i][j]
            
    return min(memo.values())

if __name__ == "__main__":
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    
    print(min_falling_path_sum(A))
