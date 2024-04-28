K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
