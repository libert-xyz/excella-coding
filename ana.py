def ana(w1,w2):

   wlist1 = list(w1)
   wlist2 = list(w2)

   wlist1.sort()
   wlist2.sort()
   matches = 0

   for i in range(len(wlist1)):
        if wlist1[i] == wlist2[i]:
            matches = matches + 1
        else:
            return False

        if matches == len(wlist2)-1:
            return True

   print (matches)

w1 = (input('Word 1: '))
w2 = (input ('word 2: '))

print (ana(w1,w2))
