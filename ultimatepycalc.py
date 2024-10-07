#My code is readable enough, anyone complaining about no comments is a cry baby
def add():
    print ("add")
    print ("Give me an x")
    x = float(input())
    print ("giveth me thy y")
    y = float(input())
    print ("the result is " +str(x+y))

def subtract():
    print ("subtracts ")
    print ("give me a number")
    x = float(input())
    print ("give me another number")
    y = float(input())
    print ("The result is " + str (x-y))

def multiply():
    print ("Multiply (only put numbers cause in the codes current state, it bugs) ")
    print ("give me a number")
    x = float(input())
    print ("give me another number")
    y = float(input())
    print ("The result is " + str (x*y))

def divide():
    print ("divide")
    print ("give me a number")
    x = float(input())
    print ("give me another number")
    y = float(input())
    print ("The result is " + str (x/y))


def greaterthan():
    print ("greater than Program by team-res")
    print ("Give me an x")
    x = float(input())
    print ("Give me a y")
    y = float(input())
    if x > y:
        print (str(x) + " is greater than " + str(y))
    elif y > x:
        print (str(y) + " is greater than " + str(x))
    else:
        print ("Both numbers are equal")

def select():
    print ("Hello")
    print ("1 to multiply      2 to divide")
    print ("3 to addition      4 to subtract")
    print ("5 to greater than")
    select = input()
    if select == "1":
        multiply()
    if select == "2":
        divide()
    if select == "3":
        add()
    if select == "4":
        subtract()
    if select == "5":
        greaterthan()
    else:
        print ("idk")

select()
print ("program ended")
