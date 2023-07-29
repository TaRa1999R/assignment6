print (" 🧮🧮 SOLVE THIRD GRADE EQUATION 🧮🧮 ")

import math 
from colorama import Fore

print (Fore.CYAN , " The shape of equation is : a*x^3 + b*x^2 + c*x + d = 0 " )
print (" Please enter a , b , c and d as inputs to get the results " , Fore.RESET )

def delta3 ( a , b , c , d ) :

    delta = ( 18*a*b*c*d ) - ( 4*(b**3)*d ) + ( (b**2)*(c**2)) - ( 4*a*(c**3) ) - ( 27*(a**2)*(b**2) )
    if delta > 0 :
        print ( Fore.BLUE , " The equation has three real roots " , Fore.RESET )
        return delta
    
    elif delta == 0 :
        print ( Fore.BLUE , " The equation has additional real roots " , Fore.RESET )
        return delta
    
    else :
        print (Fore.BLUE , " The equation has a real root and two complex roots " , Fore.RESET )
        return delta
    
def delta2 ( a , b , c ) :
    
    delta = ( b**2 ) - ( 4*a*c )
    if delta > 0 :
        print ( Fore.BLUE , " The equation has two real roots " , Fore.RESET )
        return delta
    
    elif delta == 0 :
        print ( Fore.BLUE , " The equation has one real root " , Fore.RESET )
        return delta
    
    else :
        print ( Fore.BLUE , " The equation dosen't have any answer " , Fore.RESET )
        return delta
    
a = int ( input (" Please enter a : "))
b = int ( input (" Please enter b : "))
c = int ( input (" Please enter c : "))
d = int ( input (" Please enter d : "))

if a == 0 and b != 0 :                                                             #second digree
    print ( Fore.RED , " This is a second degree equation " , Fore.RESET )
    delta = delta2 ( b , c , d )

    if delta > 0 :
        x1 = ( -b + ( math.sqrt ( delta ))) / ( 2 * a )
        x2 = ( -b - ( math.sqrt ( delta ))) / ( 2 * a )
        print ( Fore.GREEN , " The answers are : " , x1 , x2 , Fore.RESET )

    elif delta == 0 :
        x = -b / ( 2 * a )
        print ( Fore.GREEN , " The answer is : " , x , Fore.RESET )

    elif delta < 0 :
        print ( Fore.GREEN , " The equation doesn't have any answer " , Fore.RESET )


elif a == 0 and b == 0 and c != 0 :                                                #firs digree
    print ( Fore.RED , " This is a simple equation " , Fore.RESET )
    x = - d / c
    print ( Fore.GREEN , " The answer is : ", x , Fore.RESET )


elif a == 0 and b == 0 and c == 0 :                                                #not equation
    print ( Fore.RED , " This is not an equation " , Fore.RESET )


else :
    print ( Fore.RED , " This is a third grade equation " , Fore.RESET )
    delta = delta3 ( a , b , c , d )
    if delta > 0 :
        354848

    elif delta == 0 :
        687956

    elif delta < 0 :
        684652

print ( Fore.MAGENTA , " DONE " , Fore.RESET)