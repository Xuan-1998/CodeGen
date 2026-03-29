def count_diamonds(N):
    memo = {}

    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        even_sum = 0
        odd_sum = 0
        room_number = i + j

        for digit in str(room_number):
            if int(digit) % 2 == 0:
                even_sum += int(digit)
            else:
                odd_sum += int(digit)

        result = abs(even_sum - odd_sum)
        memo[(i, j)] = result
        return result

    total_diamonds = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            total_diamonds += f(i, j)

    return total_diamonds


T = int(input())
for _ in range(T):
    N = int(input())
    print(count_diamonds(N))
