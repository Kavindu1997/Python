#Number of occurrences

test = [10,2,5,10,1,5,10]

def numberOf(list, element):

    occurrences = 0

    for e in list:

        if e == element:

            occurrences = occurrences + 1

    return occurrences

print(numberOf(test, 0))