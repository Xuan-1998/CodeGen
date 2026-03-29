def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = n
        for _ in range(m):
            temp = 0
            while result > 0:
                digit = result % 10
                result //= 10
                temp = temp * 10 + (digit + 1)
            result = temp
        print(result.bit_length() % (10**9 + 7))

if __name__ == "__main__":
    solve()
