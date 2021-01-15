#is prefix

# "abcde", "ab" => True

# "abcde", "bc" => False

def isPrefix(input, prefix):

    if len(input) < len(prefix):

        return False

    i = 0

    while i < len(prefix):

        if prefix[i] != input[i]:

            return False

        i += 1

    return True



#print(isPrefix("abcde", "ab"))

#print(isPrefix("abcde", "bc"))