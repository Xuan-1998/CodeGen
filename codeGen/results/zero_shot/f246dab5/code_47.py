n = int(input())  # number of trips

fares = []
for i in range(n):
    t_i = int(input())  # time of trip i
    if i == 0 or t_i - fares[-1] >= 90:  # new ticket needed
        fares.append(50)  # use a ticket for 90 minutes
    else:
        fares.append(20)  # use a ticket for one trip

print(*fares, sep='\n')  # print the total fare for each trip
