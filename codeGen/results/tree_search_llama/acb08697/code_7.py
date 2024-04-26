n = int(input())  # read the number of operations

pile = 0  # initialize the pile with 0 stones
for op in input().strip():  # iterate over the sequence of operations
    if op == "+":  # add one stone to the pile
        pile += 1
    else:  # remove one stone from the pile
        pile -= 1

print(pile)  # print the minimum number of stones in the pile
