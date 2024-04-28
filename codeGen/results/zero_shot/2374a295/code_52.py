n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    good_sequ = 1
    for j in range(k-1):
        if (i*(j+2)) % ((j+2)*(j+3)) != 0:
            break
        good_sequ += 1
    ans += good_sequ
print(ans%1000000007)
