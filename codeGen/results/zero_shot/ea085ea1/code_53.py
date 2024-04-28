N = int(input())
str1 = input()
str2 = input()

max_count = 0
for i in range(N):
    for j in range(i+1, N):
        substr1 = str1[i:j]
        count = 0
        for k in range(N):
            if substr1 == str2[k:k+len(substr1)]:
                count += 1
        max_count = max(max_count, count)

print(max_count)
