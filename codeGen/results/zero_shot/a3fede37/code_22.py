def max_path_sum(array):
    def max_path_sum_recursive(index):
        if array[index] < 0:  
            return 0
        left_sum = max_path_sum_recursive(2 * index + 1) if 2 * index + 1 < len(array) else 0
        right_sum = max_path_sum_recursive(2 * index + 2) if 2 * index + 2 < len(array) else 0
        return array[index] + max(left_sum, right_sum)

    return max_path_sum_recursive(0)


if __name__ == "__main__":
    n = int(input())
    array = [int(x) for x in input().split()]
    print(max_path_sum(array))
