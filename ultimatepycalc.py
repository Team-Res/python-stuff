#My code is readable enough, anyone complaining about no comments is a cry baby

def multiply():
    print ("Multiply (only put numbers cause in the codes current state, it bugs) ")
    print ("give me a number")
    x = int(input())
    print ("give me another number")
    y = int(input())
    print ("The result is " + str (x*y))

def greaterthan():
    #im going to have to write a system that lets you choose between the 2, just too lazy to do that rn
    print ("greater than Program by team-res")
    print ("Give me an x")
    x = int(input())
    print ("Give me a y")
    y = int(input())
    if x > y:
        print (str(x) + " is greater than " + str(y))
    elif y > x:
        print (str(y) + " is greater than " + str(x))
    else:
        print ("Both numbers are equal")
def select():
    print ("Hello")
    print ("1 to multiply      2 to Greater Than")
    select = input()
    if select == "1":
           multiply()
    if select == "2":
           greaterthan()
    else:
        print ("ending program")

select()
