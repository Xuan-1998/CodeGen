def count_matrices():
    T = int(input())  # read number of test cases
    results = []

    for _ in range(T):
        N = int(input())  # read trace value
        count = 0

        for a in range(1, N // 2 + 1):  # fix one diagonal element
            d = N - a  # calculate other diagonal element
            det = a * d  # calculate determinant

            if det > 0:  # check if determinant is positive
                count += 1

        results.append(count)

    for result in results:
        print(result)  # output the number of matrices

count_matrices()
