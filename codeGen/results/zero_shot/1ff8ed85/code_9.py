def can_send_over_network(b):
    n = len(b)
    for i in range(2 ** (n - 1)):
        a = []
        j = 0
        for k in range(n):
            if ((i >> k) & 1):
                a.append(str(len(a) + 1)) if not a or a[-1] != str(len(a)) else a.append('0')
                j += len(a) - int(a[-1]) if a and a[-1] != '0' else 0
            else:
                a.append(str(j))
                j = int(a[-1])
        if ''.join(a) == ''.join(map(str, b)):
            return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_over_network(b))
