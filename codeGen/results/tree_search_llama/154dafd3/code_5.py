import math

def round_to_nearest_multiple_of_five():
    n = int(input())  # Read the size of the array from standard input
    arr = [float(x) for x in input().split()]  # Read the array elements from standard input
    
    rounded_arr = []
    
    for num in arr:
        if math.modf(num)[0] >= 0.5:  # Check if the number is halfway between two multiples of 5
            rounded_arr.append(math.ceil(num) // 5 * 5 + 5)
        else:
            rounded_arr.append(math.floor(num) // 5 * 5)
    
    for num in rounded_arr:
        print(int(num), end=' ')  # Print the rounded numbers to standard output

round_to_nearest_multiple_of_five()
