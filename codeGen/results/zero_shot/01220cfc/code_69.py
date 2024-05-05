def can_reach_end(array):
    current_index = 0
    farthest_index = 0

    for jump_length in array:
        farthest_index = max(farthest_index, current_index + jump_length)
        if current_index >= len(array) - 1:
            return True
        current_index = farthest_index

    return False


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    print(can_reach_end(array))
