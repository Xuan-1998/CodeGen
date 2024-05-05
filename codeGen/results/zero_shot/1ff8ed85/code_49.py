t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    for i in range(1, len(b)):
        if b[i-1] < b[i]:
            a.append(str(b[i-1]))
        else:
            a.append(' ' + str(b[i]))
    if ''.join(a).replace(' ', '') == ''.join(map(str, b)):
        print('YES')
    else:
        print('NO')
