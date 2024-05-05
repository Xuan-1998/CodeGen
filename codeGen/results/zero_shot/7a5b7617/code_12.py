T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_table_count(N, M))
