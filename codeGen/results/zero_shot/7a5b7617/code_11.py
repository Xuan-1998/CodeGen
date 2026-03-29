def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = 0
        for i in range(N-1, -1, -1):
            if i == N-1:
                for j in range(M+1):
                    print(j)
                    if sum(range(i+1)) + j <= M:
                        break
                else:
                    continue
            for j in range(sum(range(i))+1, sum(range(i+1))+1):
                print(j)
        print(result)

solve()
