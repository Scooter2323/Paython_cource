#hardcoded - aka database
food_name  = "Salad"
food_price = 50.00
food_available = 10


# calculations
client_quantity = int(input( "How many ? ") )   # <<<<< User : enters data !!!

if client_quantity >  0  and   client_quantity <= food_available :
    food_total_cost = food_price * client_quantity
    #output 
    print ( "total cost : ", food_total_cost)
else :
    print( "Wrong value for quantity !!!" )

    # if EXPRESSION : 
    #    code for True
    #  else: 
    #    code for Falce

    # if EXPRESSION1:
    #    code for \True 
    # elif EXPRESSION2:
    #    code for True on condition2
    # elise:
    #    code for Falce






    # ins1 ---> ins2 ---> ... insN ---> <EXPRESSION ???> /---> True  ---> code for True
    #                                                    \---> Falce ---> code for Falce