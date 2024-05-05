===BEGIN CODE===
def solve():
    n = int(input())
    moods = list(map(int, input().split()))
    dp = [True]
    
    for i in range(1, n):
        if moods[i] == 1:
            dp.append(dp[-1])
        else:
            dp.append(False)
            
    print('YES' if dp[-1] else 'NO')

solve()
===END CODE===
