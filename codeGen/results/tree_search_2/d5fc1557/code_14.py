import sys

def read_array():
    return list(map(int, sys.stdin.readline().split()))

def write_answer(answer):
    print(answer)

n = int(sys.stdin.readline())
nums = read_array()

answer = longest_subarray(nums)
write_answer(answer)
