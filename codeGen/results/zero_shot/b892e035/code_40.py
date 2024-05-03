T = int(input())
for _ in range(T):
    n = int(input())
    probabilities = []
    numbers = []
    for _ in range(n):
        P, A, B = map(int, input().split())
        probabilities.append(P)
        numbers.append((A, B))

    num_ways = 1
    for i in range(n):
        num_ways *= probabilities[i]

    correct_numbering = num_ways / (2 ** n)
    print(round(correct_numbering, 6))  # Round to 10^-6 precision
