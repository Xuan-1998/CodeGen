def count_good_subseqs(a):
    n = len(a)
    subsequences = generate_subsequences(a)
    good_subseqs = 0
    for subseq in subsequences:
        if is_good_subseq(subseq):
            good_subseqs += 1
    return good_subseqs % (10**9 + 7)
