def findFirstRecChar(string):
    for i in range(len(string)):
        if string[i] in string[0:i]:
            return string[i]
    return None

def findFirstRecChar_fast(string):
    char_set = set()

    for c in string:
        if c not in char_set:
            char_set.add(c)
        else:
            return c
    return None

string = "fhnrklbenkabcbaasd"
print(findFirstRecChar(string))
print(findFirstRecChar_fast(string))
