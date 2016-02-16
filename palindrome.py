
def palin(palin_list):

    palin_rest = []
    for i in palin_list:

        reverse = i[::-1]

        if i == reverse:
            palin_rest.append(True)

        else:
            palin_rest.append(False)


    return palin_rest



lt = ['abc','kajak','dad','dady','madam','rodri','abcba']
print (palin(lt))
