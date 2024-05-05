from sys import stdin, stdout

def main():
    n = int(stdin.readline())
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n+1):
        b = bin(i)[2:]
        count = dp[i-1] if i > 0 else 1
        for j in range(len(b)):
            if b[j] == '1':
                if j > 0 and b[j-1] == '1' or j < len(b)-1 and b[j+1] == '1':
                    break
                count = dp[i-1] if i > 0 else 1
        dp[i] = count

    stdout.write(str(dp[n]))
    stdout.write('\n')

if __name__ == "__main__":
    main()
