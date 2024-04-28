n = int(input())
str1 = input().strip()
str2 = input().strip()

def solve():
    max_count = 0
    for i in range(n):
        for j in range(i+1, n):
            substr1 = str1[i:j+1]
            count = 0
            for k in range(n):
                if str2[k:k+len(substr1)] == substr1:
                    count += 1
                    k += len(substr1) - 1
            max_count = max(max_count, count)
    print(max_count)

solve()
