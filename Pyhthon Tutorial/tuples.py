thisTuple = ("banana", "cherry", "apple")

print(thisTuple)

#Tuples are used to store multiple items in a single variable.

#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

#A tuple is a collection which is ordered and unchangeable.

#Tuples are written with round brackets.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#in order to change the tuple you have to first convert it to a lost then modify it

x = (1, 2, 3)
print(x)
y = list(x)
y[1] = 0
x = tuple(y)

print(x)

#to add items you can use this method again, however, there is another way where we create another tuple and add them

z = (10, )
x += z

print(x)

# to delete the only way is converting it to a list and back to tuple again

#we can also unpack tuple elements by giving them a name 

(num1 ,num2 ,num3, num4) = x
print(num1)
print(num2)
print(num3)
print(num4)

#we can also unpack tuple elements by using * at the beginning of the variable which will convert the rest to a list

t = (0 ,1, 2 ,3 ,4, 5)
(n, n1, n2, *nr) = t
print(n)
print(n1)
print(n2)
print(nr)

# you can also use it in the middle

(nFirst, *nMiddle, nLast) = t

print(nFirst)
print(nMiddle)
print(nLast)

#you can loop the tuples as lists

#you can join tuples as list aswell, there are unique ways also

myT = t * 2 #doubles the element

print(myT)


###########################METHODS##############################
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found



