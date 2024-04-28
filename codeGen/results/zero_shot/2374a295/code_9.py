k, n = map(int, input().split())
count = 0
for i in range(1, n+1):
    flag = True
    seq = [i]
    for j in range(k-1):
        if seq[-1] == 1:
            break
        next_num = 0
        for d in range(2, int(seq[-1]**0.5) + 1):
            if seq[-1] % d == 0:
                next_num = d
                break
        else:
            next_num = seq[-1]
        if next_num > n:
            flag = False
            break
        seq.append(next_num)
    if flag:
        count += 1
print(count%1000000007)
