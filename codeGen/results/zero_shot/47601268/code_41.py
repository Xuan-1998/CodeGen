import sys
def count_binary(n):
    res = 0
    for i in range(n+1):
        binary = bin(i)[2:]
        if '11' not in binary:
            res += 1
    return res
n = int(sys.stdin.readline().strip())
print(count_binary(n))
