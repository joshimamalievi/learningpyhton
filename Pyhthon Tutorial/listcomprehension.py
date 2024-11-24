import random

fruits = ["ananas", "banana", "cherry", "kiwi"]
fwitha = []
frest = []

print("this is the whole list")
print(fruits)
#seperating the main list if there is an 'a' inside
#for x in fruits:
 #if "a" in x:
  #fwitha.append(x)
 #else:
  #frest.append(x)

#--------short
fwitha = [x.upper() for x in fruits if "a" in x]
frest = [x.upper() for x in fruits if "a" not in x]

print("after")
print(fwitha)
print(frest)

nums = [x for x in range(10) if x < 6] # creating an lsit of numbers with short hand for func 
print(nums)
randNums = [random.randrange(100) for x in range(100) ]# creating random 100 num list

print(randNums)

#sorting them
randNums.sort()
print(randNums)

#reverse sorting
randNums.sort(reverse=True)
print("Reversed: \n", randNums )

#sorting the list making a func

def myfunc(n):
  return abs(n - 50)

randNums.sort(key = myfunc)#sorts the elements by how close to 50 they are
print(randNums)

#copying list

fruit2 = fruits.copy()
#or
fruit2 = list(fruits)
#or
fruit2 = fruits[:]

print(fruit2)

#adding them together
fruitsreunitedangry = fwitha + frest

print(fruitsreunitedangry)
