import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_sum = 0
        xor_sum = 0
        for _ in range(n):
            num = int(input())
            and_sum |= num
            xor_sum ^= num
        print((xor_sum & (xor_sum - 1)) == 0)  # Check if XOR is power of 2, 
                                                  # which means the AND will be greater than or equal to the XOR
        # Here we just need to count the arrays satisfying this condition
        and_count = 0
        for i in range(2**k):
            temp_and_sum = 0
            temp_xor_sum = 0
            for j in range(n):
                num = i & ((1 << k) - 1)
                if (num >> k-j-1) & 1:  # Check if the bit is set at position j
                    temp_and_sum |= num
                    temp_xor_sum ^= num
                else:
                    temp_and_sum |= (~((1 << k) - 1))  # Flip all bits to the right of position j
                    temp_xor_sum ^= ((1 << k) - 1)
            if temp_and_sum >= temp_xor_sum:  # Check if AND is greater than or equal to XOR
                and_count += 1
        print(and_count % (10**9 + 7))
