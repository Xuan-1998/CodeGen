def next_state(val):
    n = len(str(val))
    remain = [int(digit) % 10 for digit in str(val)]
    new_remain = []    
    for d in remain:
        new_d = (d + 1) % 10
        new_remain.append(new_d)
    return n, int(''.join(map(str, new_remain)))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        n, n = next_state(n)
    print(len(str(n)) % 1000000007)
