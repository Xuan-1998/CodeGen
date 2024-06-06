function main():
    n = read_integer_from_stdin()
    array = read_array_of_integers_from_stdin()
    
    if 1 is in array:
        return the number of non-1 elements in the array
    else:
        for each pair of adjacent elements in the array:
            if GCD of the pair is 1:
                return the number of operations to make the array all 1s
        return -1
