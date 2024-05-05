# Step 1: Read the input
n = int(input())
p = list(map(int, input().split()))

# Step 2: Sort the permutation p
p.sort()

# Step 3: Check if there are two arrays a and b, each of length n, with no common elements, so that p=merge(a,b)
for i in range(n):
    if p[i] == p[n+i]:
        break
else:
    print("YES")
else:
    print("NO")
