import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        result = 0
        while m > 0:
            m -= 1
            temp = str(n)
            for i in range(len(temp)):
                digit = int(temp[i])
                if digit < 9:
                    temp = temp[:i] + str(digit+1) + temp[i+1:]
                else:
                    temp = temp[:i] + '0' + temp[i+1:]
            n = int(temp)
            result += len(str(n)) - len(str(int(temp)))
        print(result % (10**9+7))

solve()
