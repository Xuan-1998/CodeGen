def can_jump(arr):
    max_reachable = 0

    for i in range(len(arr)):
        if i > max_reachable:
            return False

        max_reachable = max(max_reachable, i + arr[i])

    return True


if __name__ == "__main__":
    arr = [2,3,1,1,4]
    print(can_jump(arr))
