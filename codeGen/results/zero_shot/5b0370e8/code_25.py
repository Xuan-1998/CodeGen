def count_arrays(n, k, integers):
    count = 0
    for i in range(2**n):
        and_result = and_operation(k)
        xor_result = sum([integers[j] ^ (1 << j) if ((i >> j) & 1) else integers[j] for j in range(n)])
        if and_result >= xor_result:
            count += 1
    return count % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    integers = list(map(int, input().split()))
    print(count_arrays(n, k, integers))
