import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Step 1: Calculate bitwise AND and XOR of all elements
    and_result = reduce(lambda x, y: x & y, a)
    xor_result = reduce(lambda x, y: x ^ y, a)
    
    # Step 2: Count the number of arrays for which bitwise AND is greater than or equal to bitwise XOR
    count = sum(1 for ai in a if (and_result >= xor_result) == (ai & and_result >= ai ^ xor_result))
    
    print(count % (10**9 + 7))
