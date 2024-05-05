def solve():
    t = int(input())  # read number of test cases
    for _ in range(t):
        n, k = map(int, input().split())  # read n and k
        arr = list(map(int, input().split()))  # read array elements
        count = 0
        for i in range(2**k):  # iterate over all possible values of bits
            and_result = i
            xor_result = 0
            for num in arr:
                and_result &= num
                xor_result ^= num
            if and_result >= xor_result:  # check the condition
                count += 1
        print(count % (10**9 + 7))  # print the result

solve()
