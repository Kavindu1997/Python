#Biggest number in List

# [8, 4, 5, 1, 0, 10] => 10

def biggest(list):

    biggest = list[0]

    i = 1

    while i < len(list):

        if biggest < list[i]:

            biggest = list[i]

        i += 1

    return biggest



#print(biggest([1,5,8,10,2,1,11]))