function gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

function min_operations(array):
    if 1 in array:
        return 0  # Already contains a 1, no operations needed
    
    total_gcd = array[0]
    for i from 1 to length(array) - 1:
        total_gcd = gcd(total_gcd, array[i])
    
    if total_gcd > 1:
        return -1  # Not possible to make all elements equal to 1
    
    operations = 0
    for each element in array:
        while element > 1:
            find adjacent element with which GCD(element, adjacent) is minimized
            replace element with GCD(element, adjacent)
            increment operations
    return operations
