T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = count_steady_tables(N, M)
    print(result)
