code_block_start
while True:
    index = s.find('AB')
    if index == -1:
        break

    next_index = index + 2
    while True:
        if s[next_index:next_index+2] == 'BA':
            print("YES")
            exit(0)
        next_index += 1
    s = s[index+2:]
code_block_end
