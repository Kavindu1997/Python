
#Reverse string

# abc => cba

#

# cba



def reverse(string):

    result = ""

    for c in string:

        result = c + result

    return result



#print(reverse("Hello"))