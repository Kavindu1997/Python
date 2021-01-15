
#number of words in String

# "bbb loo, Hello. My Fried" => 5

def numberOfWords(input):

    if len(input) == 0:

        return 0

    count = 1

    for c in input:

        if c == " ":

            count += 1

    if input[len(input) - 1] == " ":

        count -= 1

    return count



#print(numberOfWords("fff fff"))


