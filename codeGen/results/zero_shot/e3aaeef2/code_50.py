def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = 0
        while m:
            digits = [int(x) for x in str(n)]
            n = ''.join(str(i+1) if i < len(digits)-1 else '1' for i in range(len(digits)))
            m -= (9 - min(digits)) + len([x for x in digits if x > 0])
            result += 1
        print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
