def can_send_sequence(b):
    n = len(b)
    for i in range(n):
        if (b[i][0] != 1 and b[i][1] == 'left') or (b[i][0] != n and b[i][1] == 'right'):
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = [list(map(int, input().split())) for _ in range(n)]
    if can_send_sequence(b):
        print('YES')
    else:
        print('NO')
