t = int(input())  # read the number of test cases

for _ in range(t):
    n = int(input())  # read the size of the sequence b
    b = list(map(int, input().split()))  # read the sequence b
    
    for i in range(1, n):  # try different segment lengths
        a = [i] * (n - 1) + [b[-1]]  # construct sequence a
        if "".join(map(str, a)) == "".join(map(str, b)):  # check if b can be obtained from a
            print("YES")
            break
    else:
        print("NO")
