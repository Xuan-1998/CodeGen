from functools import lru_cache

@lru_cache(None)
def count_matrices(trace):
    if trace == 0:
        return 1
    elif trace < 3:
        return 0
    result = 0
    for i in range(1, (trace + 1) // 2 + 1):
        if (trace - 2 * i) % 2 == 0 and trace - 2 * i >= 0:
            j = (trace - 2 * i) // 2
            result += count_matrices(i - 1)
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
