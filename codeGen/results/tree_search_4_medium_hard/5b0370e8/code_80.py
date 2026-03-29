code = '''
def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp_and = [[0] * (1 << k) for _ in range(n + 1)]
        dp_xor = [[0] * (1 << k) for _ in range(n + 1)]

        for i in range(n):
            x = int(input())
            for j in range(1 << k):
                if (x & j) >= ((~j) >> k - 1):
                    dp_and[i + 1][j] += 1
                if (x ^ j) < (2 ** k - 1):
                    dp_xor[i + 1][j] += 1

        total_count = 0
        for j in range(1 << k):
            if dp_and[n][j] >= dp_and[n][j ^ ((1 << k) - 1)]:
                total_count += 1

        print(total_count % (10**9 + 7))

if __name__ == "__main__":
    solve()
'''

print(code)
