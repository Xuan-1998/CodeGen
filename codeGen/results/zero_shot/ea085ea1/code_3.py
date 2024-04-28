n = int(input())
str1 = input().strip()
str2 = input().strip()

count = 0
for i in range(n):
    for j in range(i+1, n):
        if str1[i:j+1] in str2 and str2.find(str1[i:j+1]) == str2.index(str1[i:j+1]):
            count += 1

print(count)
