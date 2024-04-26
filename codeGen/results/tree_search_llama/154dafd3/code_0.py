import math

def round_to_nearest_multiple_of_five(lst):
    result = []
    for num in lst:
        # Convert the number to an integer by multiplying it with 100 and then rounding off.
        # Then, convert it back to a float by dividing it by 100.
        rounded_num = float(math.floor(float(num) * 20 + 0.5)) / 10
        result.append(str(int(rounded_num * 10))))
    return result

# Read input from standard input
lst = [float(x.strip()) for x in stdin.readline().split()]

# Print the output to standard output
print("\n".join(map(str, round_to_nearest_multiple_of_five(lst))))
