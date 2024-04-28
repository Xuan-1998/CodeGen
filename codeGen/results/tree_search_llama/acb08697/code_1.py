def min_stones(n, s):
    min_stones = 1  # Initialize with a single stone
    for op in s:
        if op == '+':
            min_stones += 1
        else:  # op is '-'
            min_stones -= 1
            if min_stones < 0:
                min_stones = 0  # Don't let the pile have negative stones
    return min_stones

n = int(input())
s = input()
print(min_stones(n, s))
