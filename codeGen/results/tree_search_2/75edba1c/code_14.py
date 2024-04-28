def find_greater_max(N, K, Arr):
    has_greater_max = [False] * N
    for i in range(N - 1, -1, -1):
        if max(Arr[i:]) > K:
            has_greater_max[i] = True
        for j in range(i + 1, N):
            if Arr[j] > max(Arr[:i]):
                if has_greater_max[j]:
                    print(1)
                    return
    print(sum(has_greater_max))

N = int(input())
K = int(input())
Arr = list(map(int, input().split()))
find_greater_max(N, K, Arr)
