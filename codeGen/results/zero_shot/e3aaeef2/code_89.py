def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        res = str(n)
        while m > 0:
            new_res = ''
            for d in res:
                if d == '9':
                    new_res += '0'
                else:
                    new_res += str(int(d) + 1)
            res = new_res
            m -= 1
        print(len(str(res)) % (10**9 + 7))

if __name__ == "__main__":
    solve()
