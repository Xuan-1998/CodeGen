import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    for i in range(1, n + 1):
        if all((a[i - 1] % j == 0) for j in range(1, i)):
            res += 1
    
    print(res)

if __name__ == "__main__":
    solve()
