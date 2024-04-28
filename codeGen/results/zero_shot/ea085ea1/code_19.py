n = int(input())
str1 = input()
str2 = input()

max_common = 0
for i in range(n):
    for j in range(i+1, n+1):
        substr1 = str1[i:j]
        common_count = 0
        for k in range(len(substr1)):
            if str2.find(substr1[k:]) == -1:
                break
            common_count += 1
        max_common = max(max_common, common_count)

print(max_common)
