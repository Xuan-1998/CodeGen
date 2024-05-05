import sys

def expected_carries(n):
    total_pairs = 10 ** n * (n + 1)  # calculate the total number of pairs
    carries = 0

    for i in range(n, -1, -1):  # iterate over each digit position from right to left
        for a in range(10):  # consider all possible values for A
            for b in range(10):  # consider all possible values for B
                if (a + b) >= 10:  # check if adding A and B results in a carry
                    carries += 1  # increment the carry count

    return carries / total_pairs  # calculate the expected number of carries

T = int(sys.stdin.readline())  # read the number of test cases
for _ in range(T):
    n = int(sys.stdin.readline())  # read N, the maximum number of digits
    print(expected_carries(n))  # print the expected number of carries for this test case
