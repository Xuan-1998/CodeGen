import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [True]
    for i in range(1, n):
        total = 0
        for j in range(i-1, -1, -1):
            total += a[j]
            if total >= a[i]:
                dp.append(True)
                break
        else:
            dp.append(False)
    
    print("YES" if dp[-1] else "NO")

if __name__ == "__main__":
    solve()
