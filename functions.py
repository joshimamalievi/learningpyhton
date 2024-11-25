def myName(name, lname):
    print(name , lname)

myName("Joshgun", "Imamalievi")
myName("Martina", "Puig Gonzalez")


#if the number of parameters are unknown then we use * 

def myFam(*kid):
    print("The most handsome kid of the family is:", kid[0])

myFam("Joshgun", "Imamali")

#the same for the unknown number of key and value cariables, we use **

def lname(**kid):
    print("his lastname is", kid["lname"])

lname(name = "Joshgun", lname = "Imamalievi")

#The following example shows how to use a default parameter value.

#If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def myfunction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

myfunction(fruits)

#the return statement

def multiplywith5(num):
    return 5*num

print(multiplywith5(5))


############################Recursion
#Python also accepts function recursion, which means a defined function can call itself.

#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

#The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

#To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)