code
n = int(input())
count = 0
for i in range(n+1):
    s = bin(i)[2:]
    if '11' not in s:
        count += 1
print(count)
/code
