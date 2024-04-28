from sys import stdin

def read_binary(n):
    return int(stdin.readline().rstrip(), 2)

def xor_and_left_shift(a, b, i):
    return (a ^ ((b << i) % (10**9 + 7)))

def main():
    a = read_binary(10**5)
    b = read_binary(10**5)
    dp = {0: 0}
    
    for i in range(1, 316224):
        if i not in dp:
            continue
        for j in range(i):
            dp[i] = (dp.get(i, 0) + xor_and_left_shift(a, b, j)) % (10**9 + 7)
    
    print(dp[314159])

if __name__ == "__main__":
    main()
