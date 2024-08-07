import sys

def solve():
    n = int(sys.stdin.readline())
    count = 0
    for i in range(n + 1):
        bin_i = bin(i)[2:]  # Convert to binary, removing '0b' prefix
        has_consecutive_ones = False
        for j in range(len(bin_i) - 1):
            if bin_i[j] == '1' and bin_i[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()
