t = int(input())  # read the number of test cases

for _ in range(t):
    n = int(input())  # read the size of sequence b
    b = list(map(int, input().split()))  # read sequence b
    
    for i in range(n):  # iterate through each segment of a
        if len(str(b[i])) != b[i]:  # check if the length of the segment matches b_i
            print("NO")  # if not, it's not possible to obtain b from a
            break  # exit the loop and move on to the next test case
    else:
        print("YES")  # if we can match all elements in b, then it's possible to obtain b from a

