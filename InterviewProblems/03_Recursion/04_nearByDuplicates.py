def near_by_duplicates(s):

    if len(s) == 1:
        return s

    elif s[0] == s[1]:

        return near_by_duplicates(s[1:])

    return s[0] + near_by_duplicates(s[1:])



print(near_by_duplicates("mylleegg"))