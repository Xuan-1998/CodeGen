===BEGIN CODE===
def solve():
    t = int(input())
    memo = {}
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Apply operations
        length = 1
        val = n
        
        for i in range(m):
            new_val = 0
            carry = 0
            
            while val > 0:
                digit = val % 10
                new_val = new_val * 10 + (digit + 1) % 10
                val //= 10
                if digit < 9:
                    break
                else:
                    carry += 1
            
            if carry:
                length += 1
                val = new_val
            else:
                length -= 1
                val = new_val
        
        # Store the result in memoization
        memo[length] = val % (10**9 + 7)
        
    # Output the results
    for _ in range(t):
        n, m = map(int, input().split())
        print(memo.get(length, -1))

if __name__ == "__main__":
    solve()

===END CODE===
