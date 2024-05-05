import sys

def solve():
    n = int(sys.stdin.readline())
    count = 0
    for i in range(n+1):
        binary = bin(i)[2:]
        no_consecutive_ones = True
        consecutive_count = 0
        for j in range(len(binary)):
            if binary[j] == '1':
                consecutive_count += 1
            else:
                consecutive_count = 0
            if consecutive_count > 1:
                no_consecutive_ones = False
                break
        if no_consecutive_ones:
            count += 1
    print(count)

solve()
