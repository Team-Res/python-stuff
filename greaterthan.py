#to be merged into ultimatepycalc, im just going to have to write a system that lets you choose between them
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