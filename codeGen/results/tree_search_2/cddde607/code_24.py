K = int(input())
N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(find_paths(K, N, arr))
