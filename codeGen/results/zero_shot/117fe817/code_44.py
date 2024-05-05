def findCountOne(n):
    count = 0
    for i in range(10):
        count += min(i, n // 10**len(str(i)))
    return count

n = int(input())
print(findCountOne(n))
