A = int(input())  # read input A from stdin
B = int(input())  # read input B from stdin

for x in range(0, A // 2 + 1):  # iterate through possible values of X
    y = A - x  # calculate Y based on X and A
    if (x ^ y) == B:  # check if XOR condition is satisfied
        print(f"{x} {y}")  # print solution
