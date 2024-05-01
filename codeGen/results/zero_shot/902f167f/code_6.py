n = int(input())  # get width of rectangle
m = int(input())  # get height of rectangle

min_squares = float('inf')  # initialize minimum number of squares

for i in range(1, min(n, m) + 1):  # iterate over possible side lengths of the square
    if n % i == 0 and m % i == 0:  # check if rectangle can be tiled with this size square
        squares = (n // i) * (m // i)  # calculate number of squares required
        min_squares = min(min_squares, squares)

print(min_squares)
