a = 33
b = 33 

if a < b :
    print("Its bigger")
elif a == b:
    print("Its equal")


#this is the short hand ifelse

print(a) if a<b else print("sum:" , a + b)

#and is a keyword for 2 statements

c = 52

if a==b and c>a :
    print("c is huge")

#or on the other hand checks if one of the statements are true.

if a==b or c<a:
    print("a and b are equal")

#not checks if the statement is false

if not a==b:
    print("they not like us")
else:
    print("they like us")


#if else can be also nested

if a==b:
    print("=======================\na and b are equal")

    if  c<a:
        print("\talso bigger than c\n=======================")
    else:
        print("\thowever smaller than c\n=======================")


if b == a:# having an empty if statement like this, would raise an error without the pass statement
    pass
