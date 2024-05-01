def find_sums(nums):
    memo = {0: 0}
    unique_sums = set()
    
    for i, num in enumerate(nums):
        new_sums = set()
        
        for prev_sum in list(memo.keys()):
            memo[prev_sum + num] = memo.get(prev_sum + num, prev_sum) + num
            new_sums.add(memo[prev_sum + num])
            
        memo.update(new_sums)
    
    return ' '.join(map(str, sorted(list(unique_sums))))


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(find_sums(nums))
