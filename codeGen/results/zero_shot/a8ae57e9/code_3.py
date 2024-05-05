# Define variables
n, k = map(int, input().split())  # number of booking requests and tables
requests = []  # list to store booking requests
tables = [0] * k  # initialize table capacities

# Read in booking requests
for _ in range(n):
    request = list(map(int, input().split()))
    requests.append(request)

# Sort requests by amount spent in descending order
requests.sort(key=lambda x: x[1], reverse=True)
