n = int(input())
str1 = input().strip()
str2 = input().strip()

count = 0
for i in range(n):
    for j in range(i+1, n):
        substr1 = str1[i:j]
        if all(substr1[k] == c for k,c in zip(map(str1.__getitem__, range(i,j)), map(str2.__getitem__, range(i,j)))) and all(k < k2 or c == c2 for k,k2,c,c2 in zip(range(i,j),range(i+1,j),map(str1.__getitem__,range(i,j)),map(str2.__getitem__,range(i,j)))):
            count += 1

print(count)
