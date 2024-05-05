input_array = [int(x) for x in input().split()]
lis = [1] * len(input_array)
for i in range(1, len(input_array)):
    for j in range(i):
        if input_array[i] > input_array[j]:
            lis[i] = max(lis[i], lis[j] + 1)
print(max(lis))
