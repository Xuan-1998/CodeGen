def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = str(n)
        while m > 0:
            new_result = ''
            for d in result:
                new_d = str((int(d) + 1) % 10)
                new_result += new_d
            result = new_result
            m -= 1
        print(len(result) % (10**9 + 7))

solve()
