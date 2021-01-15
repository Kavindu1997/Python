# is sorted:

# [10, 11, 9] => False

# [1, 2, 3] => True



def isSorted(list):

    i = 0

    while i < len(list) - 1:

        if list[i] > list[i+1]:

            return False

        i += 1

    return True



print(isSorted([10, 11, 9]))



print(isSorted([10, 11, 12]))
