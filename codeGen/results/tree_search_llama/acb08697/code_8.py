n = int(input())  # read the number of operations
ops = input()  # read the sequence of operations

# initialize the pile size and removal count
pile_size = 0
removals = 0

for op in ops:  # iterate through the operations
    if op == '-':  # remove a stone
        removals += 1
    else:  # add a stone
        pile_size += 1

# calculate the minimum possible pile size
min_pile_size = pile_size - removals

print(min_pile_size)  # print the result
