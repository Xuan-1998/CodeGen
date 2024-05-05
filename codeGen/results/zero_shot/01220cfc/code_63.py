def can_jump(array):
    last_position = len(array) - 1

    for i in range(len(array) - 1, -1, -1):
        if i > last_position:
            return False
        if i + array[i] >= last_position:
            last_position = i

    return True

array_length = int(input())
array_elements = list(map(int, input().split()))

print(can_jump(array_elements))
