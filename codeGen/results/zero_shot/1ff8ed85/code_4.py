t = int(input())  # read number of test cases

for _ in range(t):
    n = int(input())  # read size of sequence b
    b = list(map(int, input().split()))  # read sequence b

    a_valid = False
    for i in range(1, n):  # iterate over all elements in b
        if abs(b[i] - (b[i-1] + 1)) > 1:  # check if element is not a valid segment length
            break  # if not, we can't split a into segments that form b, so exit loop
    else:
        a_valid = True

    print("YES" if a_valid else "NO")  # print result
