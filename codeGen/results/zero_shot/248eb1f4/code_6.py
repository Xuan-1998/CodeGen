def find_winners():
    T = int(input())  # read the number of test cases
    for _ in range(T):
        M, X = map(int, input().split())  # read M and X
        winners = []
        for i in range(1, X+1):
            if i % (M+1) == 0:  # simplified game: coin is passed once around the circle
                winners.append(i)
        print(*winners, sep=' ')

find_winners()
