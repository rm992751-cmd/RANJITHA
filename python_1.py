a = int(input ("a:"))
b = int(input ("b:"))
operation = input("add, sub, mul, dev" )
if( operation== "add"):
    print(a+b)
elif (operation=="sub"):
    print (a-b)
elif (operation=="mul" ):
    print(a*b)
elif (operation=="dev"):
    print (a/b)
else :
    print ("not valid")
