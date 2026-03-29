import sys

def solve():
    t = int(input())
    memo = {}

    for _ in range(t):
        n, m = map(int, input().split())

        def applyOp(n, m, memo):
            if (n, m) in memo:
                return memo[(n, m)]

            l, v = 1, n
            while m > 0:
                new_v = ''
                for d in str(v):
                    new_d = str(int(d) + 1)
                    new_v += new_d
                l, v = len(str(new_v)) + (l - 1), int(new_v) % (10**9 + 7)
                m -= 1

            memo[(n, m)] = l, v
            return l, v

        _, res = applyOp(n, m, memo)
        print(res)

if __name__ == "__main__":
    solve()
