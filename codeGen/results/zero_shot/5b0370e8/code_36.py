import sys
from functools import reduce

def main():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        
        count = 0
        
        for _ in range(n):
            num = int(sys.stdin.readline().strip())
            
            and_result = reduce(lambda a, b: a & b, [num] * (k.bit_length() - len(bin(num)) + 1))
            xor_result = reduce(lambda a, b: a ^ b, [num] * (k.bit_length() - len(bin(num)) + 1))
            
            if and_result >= xor_result:
                count += 1
        
        print(count % (10**9 + 7))

if __name__ == "__main__":
    main()
