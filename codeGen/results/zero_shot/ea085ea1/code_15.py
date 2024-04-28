n = int(input())
str1 = input()
str2 = input()

max_common = 0
for i in range(n):
    for j in range(i+1, n):
        substr1 = str1[i:j+1]
        common_count = sum((substr1 == c)*1 for c in str2)
        if common_count > max_common:
            max_common = common_count

print(max_common)
