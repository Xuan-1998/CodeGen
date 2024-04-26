# Receive inputs from stdin
a = int(input())
b = int(input())

# Create a range of numbers from 'a' to 'b', inclusive
range_numbers = list(range(a, b+1))

# Print the sequence to stdout
for num in range_numbers:
    print(num)
