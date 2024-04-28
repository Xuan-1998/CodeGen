n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    temp = [i]
    for j in range(k-1):
        if temp[-1] % (temp[-2]+1) == 0:
            temp.append(temp[-1]* (temp[-2]+1))
        else:
            break
    else:
        count += 1

print(count % 100000007)
