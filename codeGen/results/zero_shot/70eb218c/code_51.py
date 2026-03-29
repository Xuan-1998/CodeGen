import math

while True:
    n = int(input())  # read n from stdin
    x = int(input())  # read x from stdin
    
    if x < 10**(n-1):  # check if x is within the constraint range
        break
    
    current_len = math.floor(math.log10(x)) + 1  # calculate current length of x's decimal representation
    
    if current_len == n:
        print(0)  # no operations needed
    else:
        diff = abs(current_len - n)  # calculate the difference between current length and target length
        print(diff)  # print the minimum number of operations required
