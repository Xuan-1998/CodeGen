import sys
n = int(sys.stdin.readline())
count = 0
for i in range(n+1):
    count += str(i).count('1')
print(count)
