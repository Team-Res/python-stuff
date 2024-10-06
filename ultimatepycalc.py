#My code is readable enough, anyone complaining about no comments is a cry bab
#Decimals are also not supported
def add():
    print ("add")
    print ("Give me an x")
    x = int(input())
    print ("giveth me thy y")
    y = int(input())
    print ("the result is " +str(x+y))

def multiply():
    print ("Multiply (only put numbers cause in the codes current state, it bugs) ")
    print ("give me a number")
    x = int(input())
    print ("give me another number")
    y = int(input())
    print ("The result is " + str (x*y))

def greaterthan():
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
    print ("3 to addition")
    select = input()
    if select == "1":
        multiply()
    if select == "2":
        greaterthan()
    if select == "3":
        add()
    else:
        print ("error: no letters or floats")

select()
print ("program ended")
