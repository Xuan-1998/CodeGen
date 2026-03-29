def max_score(array):
    n = len(array)
    k = int(input())
    z = int(input())

    dp = {(i, 0): array[i] for i in range(1, n+1)}

    for _ in range(k):
        new_dp = {}
        for i in range(z, n+1):
            if i == z:
                new_dp[(i-1, i)] = max(new_dp.get((i-2, i-1), 0) + array[i], dp[(i, i)])
            elif i > z:
                new_dp[(i-1, i)] = max(new_dp.get((i-2, i-1), 0) + array[i], dp[(i, i)])
        dp = new_dp

    return max(dp.values())

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    print(max_score(list(map(int, input().split()))))
