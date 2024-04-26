import sys

while True:
    try:
        N = int(sys.stdin.readline().strip())
        S = sys.stdin.readline().strip()
        count_0, count_1 = 0, 0
        for i in range(N):
            if S[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

        if abs(count_0 - count_1) <= 1:
            print('YES')
        else:
            print('NO')
    except:
        break
