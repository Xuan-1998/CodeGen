import math

n = int(input())  # read input from stdin

count = 0
for i in range(n+1):
    if not any(str(i).zfill(math.ceil(math.log2(i))+1)[j:j+2].count('1') == 2 for j in range(len(str(i))-1)):
        count += 1

print(count)  # print the answer to stdout
