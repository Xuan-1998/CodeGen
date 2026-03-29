    total = sum(scores)
    left, right = scores[0], scores[-1]
    for i in range(1, k + 1):
        if z > 0:
            if scores[i - 1] < scores[i]:  # move to the left
                scores[i - 1] += left
                left -= 1
                z -= 1
            else:  # move to the right
                total += right
                right -= scores[-i]
        elif i % 2 == 0:
            if scores[i - 1] < scores[i]:  # move to the left
                scores[i - 1] += left
                left -= 1
            else:  # move to the right
                total += right
                right -= scores[-i]
        else:
            if scores[i - 1] > scores[i]:  # move to the right
                total += right
                right -= scores[-i]
            else:  # move to the left
                scores[i - 1] += left
                left -= 1

    print(total)  # output the maximum score for this test case
