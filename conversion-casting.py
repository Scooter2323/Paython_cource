# food order app
price__pizza = 70.50   # u.c.
price__salad = 20.00   # U.C.
price__soup  = 15.00   # U.C.

q_pizza =  int (input ( "how many pizzas ?: " )
q_salad =  int ( input ( "how many salad ?: " )
q_soup  =  int ( input ("how many soup ?: " )

cost = price__pizza * q_pizza +\
       price__salad * q_salad +\
       price__soup  * q_soup 

print( "total cost:" ,cost , "U.C.") 