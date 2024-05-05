def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = {(n, False): 0 for n in range(N + 1)}
        for carry in [False]:
            for n in range(10):
                if n >= 5:
                    dp[(N - (N // 2), carry or (n > 4))] += 1
        print(sum(dp.values()) / (N ** 2))
