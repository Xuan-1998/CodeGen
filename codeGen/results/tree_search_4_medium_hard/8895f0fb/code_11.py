def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        carries = 0
        for i in range(N):
            for j in range(N):
                if (int(str(i) + str(j)) % 10 >= 5 or int(str(i) + str(j)) % 10 == 9):
                    carries += 1
        print(carries / (N * N))
