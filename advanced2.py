def eval_temperature( temp ):
    if temp >= 50:
        print( temp , " => Very HOT!" )
    if temp >= 30 and temp <   50:
        print( temp,  " => HOT!" )    
    if temp >= 10 and temp <   30:
        print( temp,  " => WARM!" )
    if temp >= -10 and temp <  10:
        print( temp,  " => COLD!" ) 
    if temp >= -30 and temp < -10:
        print( temp,  " => VERY COLD!" )  
    if temp >= -50 and temp < -30:
        print( temp,  " => VERY VERY COLD!" )    

    # HW: continue the logic .. -50 ..  
    #      hint: if  - elif - else  

#  --------------------------------------50----->
# 
# # call - testing
eval_temperature  (60) 
eval_temperature  (40)
eval_temperature  (20) 
eval_temperature  (0)
eval_temperature(-10)
eval_temperature(-40)               