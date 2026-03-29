def has_consecutive_ones(x):
    if x == 0:
        return False
    elif x & 1:  # x is odd (ends with 1)
        return not has_consecutive_ones(x >> 1)
    else:  # x is even (ends with 0)
        return True

def count_no_consecutive_ones(n):
    count = 0
    for x in range(n + 1):
        if not has_consecutive_ones(x):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())  # read input from stdin
    print(count_no_consecutive_ones(n))  # print the answer to stdout
