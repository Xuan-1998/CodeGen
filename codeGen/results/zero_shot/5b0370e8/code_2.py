import sys
from math import log2

t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # read n and k for each test case
    arr = list(map(int, input().split()))  # read array elements
    
    # calculate bitwise AND and XOR results
    and_result = 2**k - 1  # all bits set to 1 in binary representation of 2^k - 1
    xor_result = sum(x ^ (2**k - 1) for x in arr)
    
    count = 0
    if and_result >= xor_result:  # condition satisfied
        for i in range(n):
            for j in range(i + 1, n):
                temp_xor = xor_result - (arr[i] ^ arr[j])
                temp_and = and_result
                if temp_xor < temp_and:  # bitwise XOR result smaller than AND result
                    count += 1
    
    print(count % (10**9 + 7))  # print the count modulo 10^9+7
