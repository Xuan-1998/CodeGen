import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        digits = [int(x) for x in str(n)]
        for _ in range(m):
            for i in range(len(digits)):
                if digits[i] < 9:
                    digits[i] += 1
                    break
                else:
                    digits[i] = 0
        print(len(str(int(''.join(map(str, digits))))) % (10**9 + 7))

if __name__ == "__main__":
    solve()
