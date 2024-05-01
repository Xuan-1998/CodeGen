K = int(input())  # Input K
N = int(input())  # Input N
arr = [[int(x) for x in input().split()] for _ in range(N)]  # Input 2D matrix arr

print(numPathsWithExactlyKCoins(K, N, arr))
