def can_send_sequence(b):
    n = len(b)
    for i in range(1, n+1):
        a = [str(len(b[:i]))] + b[:i]
        if ''.join(map(str, a)) == ''.join(map(str, b)):
            return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_sequence(b))
