# Read input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Step 1: Calculate bitwise AND and XOR of all elements
    and_result = 0xffffffffffffffe >> (32 - k)
    xor_result = sum(xor(x, y) for x, y in combinations(arr, len(arr)))
    
    # Step 2: Count arrays where bitwise AND is greater than or equal to bitwise XOR
    count = 0
    for i in range(1 << k):
        if bin(i)[2:].zfill(k).endswith(and_result) and bin(i)[2:].zfill(k).endswith(xor_result):
            count += 1
    
    # Step 3: Print the count modulo 10^9+7
    print((count % (10**9 + 7)))
