def max_problems_to_solve():
    n, k = map(int, input().split())
    difficulties = list(map(int, input().split()))

    leftmost_index = 0
    rightmost_index = n - 1
    problems_solved = 0

    while leftmost_index <= rightmost_index:
        if difficulties[leftmost_index] <= k and difficulties[rightmost_index] <= k:
            # Choose the smallest difficulty problem
            if difficulties[leftmost_index] < difficulties[rightmost_index]:
                problems_solved += 1
                k -= difficulties[leftmost_index]
                leftmost_index += 1
            else:
                problems_solved += 1
                k -= difficulties[rightmost_index]
                rightmost_index -= 1
        elif difficulties[leftmost_index] <= k:
            # Choose the leftmost problem
            problems_solved += 1
            k -= difficulties[leftmost_index]
            leftmost_index += 1
        else:
            # Choose the rightmost problem
            problems_solved += 1
            k -= difficulties[rightmost_index]
            rightmost_index -= 1

    print(problems_solved)

max_problems_to_solve()
