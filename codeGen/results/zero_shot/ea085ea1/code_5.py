n = int(input())
s1, s2 = input().split(), input().split()

max_count = 0
for i in range(n):
    for j in range(i+1, n):
        if s1[i] == s2[j]:
            common_substr_len = 1
            while i + common_substr_len <= n and j + common_substr_len <= n:
                if s1[i:i+common_substr_len] == s2[j:j+common_substr_len]:
                    max_count += 1
                    i, j = j, i
                else: 
                    break

print(max_count)
