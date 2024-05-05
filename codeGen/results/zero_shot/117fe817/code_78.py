import math

n = int(input())  # read input from stdin

count = 0
for i in range(n + 1):
    count += math.floor(math.log10(i)) + 1

print(count)  # print output to stdout
