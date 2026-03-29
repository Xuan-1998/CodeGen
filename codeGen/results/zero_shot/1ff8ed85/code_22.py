def can_send_over_network(b):
    for i in range(1 << len(b)):
        a = [0] * (len(b) + sum(bin(i)[2:]).count('1'))
        j = 0
        for k in bin(i)[2:]:
            if k == '1':
                a[j] = b[j]
                j += 1
        if ''.join(map(str, a)) == ''.join(map(str, b)):
            return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_over_network(b))
