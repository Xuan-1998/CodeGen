def min_steps_to_color_text(text, strings):
    n = len(strings)
    m = 0  # initialize minimum steps
    used_strings = []  # store indices of used strings

    for i in range(len(text)):
        found = False
        for j in range(n):
            if text[i:].startswith(strings[j]):
                lcp_len = 0
                while i + lcp_len < len(text) and i + lcp_len <= len(strings[j]) - 1:
                    if text[i+lcp_len] == strings[j][lcp_len]:
                        lcp_len += 1
                    else:
                        break
                if lcp_len > 0:
                    m += 1
                    used_strings.append((j, i))
                    found = True
                    break
        if not found:
            return -1

    print(m)

    for i in range(len(used_strings)):
        print(f"{used_strings[i][0]} {used_strings[i][1]}")
