t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result_length = get_length_after_m_operations(n, m)
    print(result_length % (10**9 + 7))
