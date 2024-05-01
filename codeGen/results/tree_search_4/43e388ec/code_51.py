import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    
    dp = [0] * 32000  # 2^15 should be enough
    
    res = 0
    for i in range(15):
        res += ((a & (1 << i)) ^ (b >> (14 - i))) % 1000000007
        res %= 1000000007
    
    print(res)

if __name__ == "__main__":
    solve()
