# let's start by thinking about the steps we need to take
# first, we can sort the strings based on their costs and lengths

from functools import cmp_to_key
n = int(input())  # get the number of strings
costs = []  # list of costs for each string
strings = []  # list of strings themselves

for i in range(n):
    cost, s = input().split()  # split the input into cost and string
    costs.append(int(cost))  # add cost to our list
    strings.append(s)  # add string to our list

# now we need a way to sort these based on their lengths and costs
# we can compare two tuples, where each tuple is (cost, length, string)
def compare(t1, t2):
    if t1[0] < t2[0]:  # if cost is lower for the first one, return -1
        return -1
    elif t1[0] > t2[0]:  # if cost is higher for the first one, return 1
        return 1
    else:  # if costs are equal, compare lengths
        if len(t1[2]) < len(t2[2]):  # shorter string goes first
            return -1
        elif len(t1[2]) > len(t2[2]):  # longer string goes second
            return 1
        else:  # strings are the same length, so just compare them lexicographically
            if t1[2] < t2[2]:
                return -1
            elif t1[2] > t2[2]:
                return 1
            else:
                return 0

costs_and_strings = list(zip(costs, strings))  # zip the costs and strings together into tuples
sorted_costs_and_strings = sorted(costs_and_strings, key=cmp_to_key(compare))

total_cost = 0  # our total cost will be 0 initially
for i in range(n):
    if i > 0:  # for each string except the first one, we'll add its cost to the total
        total_cost += sorted_costs_and_strings[i][0]
    if strings.index(sorted_costs_and_strings[i][1]) < i:
        return -1  # if a string is in the wrong position, it's not possible to sort them

print(total_cost)  # print our final answer
