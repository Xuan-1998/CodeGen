def num_good_sequences():
    n, k = map(int, input().split())
    dp = {}

    for i in range(1, n+1):
        for j in range(i, k+1):
            if i % j == 0:
                if (i, j) not in dp:
                    dp[(i, j)] = 1
                else:
                    dp[(i, j)] += 1

    total_sequences = sum(1 for x in dp.values() if x > 0)
    print(total_sequences % 10000007)

num_good_sequences()
