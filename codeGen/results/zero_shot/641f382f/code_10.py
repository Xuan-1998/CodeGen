function find_min_operations(array):
    if 1 in array:
        return 0
    if gcd_of_all_elements(array) > 1:
        return -1
    min_operations = some_large_number
    for each pair (i, j) in array:
        if gcd(array[i], array[j]) == 1:
            operations = calculate_operations_to_make_ones(array, i, j)
            min_operations = min(min_operations, operations)
    return min_operations

function calculate_operations_to_make_ones(array, start, end):
    Implement a dynamic programming approach or other efficient method to calculate the minimum number of operations needed to make all elements between start and end equal to 1, considering that gcd(array[start], array[end]) == 1.
    return number_of_operations
