print (" 🐢🐢 DRAW A TURTLE 🐢🐢 ")

import turtle 

turtle.bgcolor ("green")
p = turtle.Pen ()
p.shape ("turtle")
p.speed ( 20 )
p.width (2)

def oval ( rad , color ) :
    p.color ( "black" , color )
    p.begin_fill ()
    for i in range ( 2 ) :
        p.circle ( rad , 90 )
        p.circle ( rad / 2 , 90 )
    
    p.end_fill ()

def dot ( rad , color ) :
    p.color ( "black" , color )
    p.begin_fill ()
    p.circle ( rad )
    p.end_fill ()


p.seth ( -45 )

oval ( 100 , "light green" )                          #lak

for i in range ( 5 , 80 , 22 ) :
    p.up ()
    p.goto ( i , i )
    p.down ()
    dot ( 10 , "dark green" )

for i in range ( 0 , 30 , 20 ) :
    p.up ()
    p.goto ( i , i + 50 )
    p.down ()
    dot ( 10 , "dark green" )

for i in range ( 35 , 120 , 22 ) :
    p.up ()
    p.goto ( i , i - 50 )
    p.down ()
    dot ( 10 , "dark green" )

for i in range ( 80 , 140 , 22 ) :
    p.up ()
    p.goto ( i , i - 100 )
    p.down ()
    dot ( 10 , "dark green" )

p.up ()                                             #surat
p.color ("black")
p.goto ( 154 , 25 )
p.down ()
p.circle ( 30 , 290 )

p.up ()                                             #cheshma
p.goto ( 180 , 40 )
p.down ()
dot ( 4 , "black")
p.up ()
p.goto ( 180 , 55 )
p.down ()
dot ( 4 , "black")

p.up ()                                            #first leg
p.goto ( 10 , -10 )
p.down ()
p.circle ( 20 , 185 )


p.up ()                                           #second leg
p.goto ( 130 , -25 )
p.down ()
p.circle ( 20 , 45 )
p.up ()
p.circle ( 20 , 180 )
p.down ()
p.circle ( 20 , 150 )


p.up ()                                            #third leg
p.goto ( 130 , 80 )
p.down ()
p.circle ( 25 , 150 )

p.up ()                                            #fourth leg
p.goto ( 10 , 100 )
p.down ()
p.circle ( 20 , 62 )
p.up ()
p.circle ( 20 , 179 )
p.down ()
p.circle ( 20 , 120 )

p.up ()
p.goto ( -15 , 26 )
p.down ()
p.goto ( -30 , 36 )
p.down ()
p.goto ( -15 , 46 )

p.up ()
p.goto ( -25 , -25 )
turtle.done ()