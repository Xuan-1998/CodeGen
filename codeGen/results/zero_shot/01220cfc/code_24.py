from sys import stdin

input_array = list(map(int, stdin.readline().split()))
n = len(input_array)

current_position = 0

for jump_length in input_array:
    if current_position + jump_length >= n - 1:
        break
    current_position += jump_length

print(current_position >= n - 1)
