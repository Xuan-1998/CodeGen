import sys

def steady_table_count():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        total_sum = (N + 1) * (M // 2 + 1)
        modulo_result = pow(10**9 + 7, total_sum, 10**9 + 7)
        print(modulo_result)

steady_table_count()
