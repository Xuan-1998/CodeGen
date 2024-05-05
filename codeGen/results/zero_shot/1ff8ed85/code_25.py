t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    for i in range(n):
        if sum([1] + [int(str(i+1) * '0' + str(j)) for j in range(1, len(str(b[i])) + 1)]) != b[i]:
            print('NO')
            break
    else:
        print('YES')
