def max_length(i):
    if i < 0:
        return 0
    if nums[i] == 0:
        return max_length(i - 1)
    else:
        length = 1
        while i > 0 and nums[i - 1] == 1:
            i -= 1
            length += 1
        return max(length, max_length(i - 1))


def main():
    n = int(input())
    global nums
    nums = [int(x) for x in input().split()]
    
    print(max_length(n-1))


if __name__ == "__main__":
    main()
