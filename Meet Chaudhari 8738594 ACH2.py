print(" please enter any small alphabet or big alphabet ")

Alpha = str(input( "write any alphabet "))

if((Alpha >= 'a' and Alpha <= 'z') or (Alpha >= 'A' and Alpha <= 'Z')):

   if (Alpha == str.lower(Alpha)):

    print("output you get is:" + str.upper(Alpha))

   elif(Alpha == str.upper(Alpha)):

    print("output you get is:" + str.lower(Alpha))

else:
    print (" only alphabet is allowed ")    

         