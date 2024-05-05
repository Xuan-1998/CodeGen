n = int(input().split()[0])
x = int(input().split()[1])

length_x = len(str(x))

diff = n - length_x
if diff < 0:
    print(-1)  # if the desired length is shorter than the current length, it's impossible to reach
else:
    print(diff)
