def solve():
    t = int(input())  # read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # read n and m
        res = n
        for _ in range(m):
            res_len = len(str(res))
            count = 0
            while True:
                res = int(str(res)[1:] + str((int(str(res)[-1]) + 1) % 10))
                if len(str(res)) == res_len:
                    break
                count += 1
            print(count % (10**9 + 7))

solve()
