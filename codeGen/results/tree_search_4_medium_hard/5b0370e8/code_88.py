import sys

# Define the modulo value
MOD = 10**9 + 7

def solve():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        # Initialize dynamic programming tables
        dp_and = [0] * (1 << k)
        dp_xor = [0] * (1 << k)
        
        for i in range(2**k):
            and_val = i
            xor_val = 0
            count = 0
            
            for j in range(n):
                if ((and_val >> j) & 1):
                    count += 1
                xor_val ^= 1 << j
            
            dp_and[and_val] = (dp_and[and_val] + 1) % MOD
            dp_xor[xor_val] = (dp_xor[xor_val] + 1) % MOD
        
        result = 0
        for i in range(2**k):
            and_val = i
            count = dp_and[and_val]
            
            # Calculate the number of arrays that satisfy the condition
            for j in range(n):
                if ((and_val >> j) & 1):
                    count = (count * (j + 1)) % MOD
            
            result = (result + count) % MOD
        
        print(result)

if __name__ == "__main__":
    solve()
