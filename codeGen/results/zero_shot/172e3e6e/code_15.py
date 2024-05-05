# Read input
n = int(input())
a = list(map(int, input().split()))

# Sort the array
a.sort()

# Initialize variables
ans = 0
i = 1
j = 0
while j < n:
    if a[j] % i != 0 or (j + 1) % i == 0: 
        while j + 1 < n and a[j + 1] % i == 0:
            j += 1
        i += 1
    else:
        ans += 1
        j += i

print(ans)
