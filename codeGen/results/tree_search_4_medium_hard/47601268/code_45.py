import sys

def solve():
    n = int(sys.stdin.readline().strip())
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        prev_bit = 0
        count = 0
        bin_i = bin(i)[2:]
        
        for j in range(len(bin_i)):
            if bin_i[j] == '1' and prev_bit == '1':
                break
            prev_bit = bin_i[j]
            count += 1
        
        dp[i] = count

    print(sum(dp))

if __name__ == "__main__":
    solve()
