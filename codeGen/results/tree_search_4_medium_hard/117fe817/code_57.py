def findOnes(n):
    memo = {0: 0}
    
    for i in range(1, len(str(n)) + 1):
        if i == 1:
            memo[i] = 1
        else:
            last_changed_bit = min(i - 2, int('1' * (i - 1), 2))
            ones_at_last_changed_bit = memo.get(last_changed_bit, 0)
            new_ones = ones_at_last_changed_bit + i
            memo[i] = new_ones
    
    total_ones = sum(memo.values())
    return total_ones

def main():
    n = int(input())
    print(findOnes(n))

if __name__ == "__main__":
    main()
