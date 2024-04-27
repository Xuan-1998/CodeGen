from collections import Counter

for _ in range(int(input())):
    N = int(input())
    S = input()
    
    count = Counter(S)
    
    if sum(count.values()) > N // 2:
        print('NO')
    else:
        print('YES')

