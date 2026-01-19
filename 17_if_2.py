# write a program to find out whether given shape is square or portrait or landscape using user given length and width 

length = int(input("Enter length"))
width = int(input("Enter width"))

#square length and width same 
if length==width: # == != < > <= >=
    print("given shape is square")

if length>width:
    print("given shape is portrait")

if length<width:
    print("given shape is landscape")

print("Good bye.")