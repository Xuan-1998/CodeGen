code block
n = int(input())
signs = list(map(int, input()))
positive_sum = 0
negative_sum = 0
for i in range(n):
    if signs[i] == 1:
        positive_sum += 1
    else:
        negative_sum += 1

print(positive_sum)
print(negative_sum)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    positive_in_range = sum(signs[i] == 1 for i in range(l-1, r))
    negative_in_range = sum(signs[i] == -1 for i in range(l-1, r))
    if positive_in_range > negative_in_range:
        print(positive_in_range - negative_in_range)
    elif positive_in_range < negative_in_range:
        print(negative_in_range - positive_in_range)
    else:
        print(0)

