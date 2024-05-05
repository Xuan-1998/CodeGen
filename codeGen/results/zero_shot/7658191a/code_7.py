def max_score():
    t = int(input())  # number of test cases
    for _ in range(t):
        n, k, z = map(int, input().split())  # number of elements, moves, and maximum moves left
        arr = list(map(int, input().split()))  # array of values

        max_score = sum(arr[:k])  # initialize the maximum score with the sum of the first k elements

        for i in range(k):  # iterate over each move
            if i >= z:  # after z moves left, we can start moving right again
                max_score += arr[i + z]  # add the value at the next index to the maximum score
            else:
                max_score -= arr[k - 1 - i]  # subtract the value at the previous index from the maximum score

        print(max_score)  # output the maximum score

max_score()
