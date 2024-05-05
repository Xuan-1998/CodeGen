def can_form_polygon(moods):
    memo = {}
    def helper(k, even_count):
        if (k, even_count) in memo:
            return memo[(k, even_count)]
        if k == 0 and even_count % 2 == 1:
            return "YES"
        if k == 0 or (even_count == 1 and k > 0):
            return "NO"
        prev_mood = moods[k-1]
        if prev_mood == moods[0]:
            if even_count % 2 == 1:
                result = helper(k-1, not even_count)
            else:
                result = "YES"
        else:
            if k % 3 != 0:
                result = "NO"
            elif (even_count + prev_mood) % 2 == 1:
                result = helper(k-1, not even_count)
            else:
                result = "YES"
        memo[(k, even_count)] = result
        return result

    n = int(input())
    moods = list(map(int, input().split()))
    print(helper(n, moods[0] == 0))
