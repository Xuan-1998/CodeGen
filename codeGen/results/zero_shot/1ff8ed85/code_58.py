t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of sequence b
    b = list(map(int, input().split()))  # sequence b itself

    a = []  # initialize a as an empty list
    cum_sum = 0  # initialize cumulative sum

    for bi in b:
        if cum_sum + bi > bi:  # if the current segment would exceed its length
            print("NO")
            break
        cum_sum += bi
        a.append(cum_sum)  # reconstruct a by concatenating segments

    else:
        print("YES")  # if we reached here, it means a was successfully reconstructed
