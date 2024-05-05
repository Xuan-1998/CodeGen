n = int(input())  # receive input integer n

count = 0
for i in range(n+1):  # consider numbers from 0 to n
    str_i = str(i)  # convert number to string
    count += str_i.count('1')  # count the occurrences of digit 1

print(count)  # print the total count
