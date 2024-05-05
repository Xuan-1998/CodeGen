import sys

def solve():
    n = int(sys.stdin.readline())
    
    count = 0
    for i in range(n+1):
        if has_consecutive_ones(i) == False:
            count += 1
            
    print(count)

def has_consecutive_ones(num):
    bin_num = bin(num)[2:]
    for i in range(len(bin_num)-1):
        if bin_num[i] == '1' and bin_num[i+1] == '1':
            return True
    return False

if __name__ == "__main__":
    solve()
