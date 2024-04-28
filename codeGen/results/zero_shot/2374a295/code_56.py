n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    if i == 1:
        count += 1
    else:
        flag = True
        for j in range(k-1):
            if i % ((j+1)+1) != 0:
                flag = False
                break
        if flag:
            count += 1
print(count % 10000007)
