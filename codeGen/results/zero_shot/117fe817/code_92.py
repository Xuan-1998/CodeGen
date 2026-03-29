def findCount(n):
    count = 0
    for i in range(1, n+1):
        if i % 10 == 1 or i % 5 == 1:
            count += 1
    print(count)

n = int(input())
findCount(n)
