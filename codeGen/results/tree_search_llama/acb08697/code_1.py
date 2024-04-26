def min_pile_size(n, s):
    x = 0  # initial pile size is 0
    for i in range(n):
        x += (-1) * int(s[i])  # apply the current operation
    return abs(x)  # return the minimal possible pile size

n = int(input())
s = input()
print(min_pile_size(n, s))
