n = int(input())
str1 = input().strip()
str2 = input().strip()

count = 0
for i in range(n):
    for j in range(i+1, n):
        substr1 = str1[i:j+1]
        if substr1 in str2:
            count += 1

print(count)
