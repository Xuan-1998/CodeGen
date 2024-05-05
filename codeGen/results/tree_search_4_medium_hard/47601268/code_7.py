import sys

def solve(n):
    memo = {}
    def dp(i, prev_zero_count=0):
        if (i, prev_zero_count) in memo:
            return memo[(i, prev_zero_count)]
        
        result = False
        binary_i = bin(i)[2:]
        for bit in binary_i:
            if bit == '1':
                if prev_zero_count > 0:
                    result = True
                    break
                else:
                    prev_zero_count += 1
            else:
                prev_zero_count = 0
        
        memo[(i, prev_zero_count)] = result
        return result

    count = 0
    for i in range(n+1):
        if not dp(i):
            count += 1
    
    print(count)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    solve(n)
