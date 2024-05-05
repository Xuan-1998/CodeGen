def can_reach_last_index():
    n = int(input())  # read array length from standard input
    arr = list(map(int, input().split()))  # read array elements from standard input

    last_index = n - 1  # the last index we want to reach
    current_index = 0  # our starting position

    while current_index < last_index:  # as long as we haven't reached the last index yet
        jump_length = arr[current_index]  # get the maximum jump length at this position
        next_index = min(last_index, current_index + jump_length)  # calculate the next possible index
        if next_index == last_index:  # if we can reach the last index from here
            return True
        current_index += 1  # move to the next position

    return False  # if we couldn't reach the last index, return False

print(can_reach_last_index())
