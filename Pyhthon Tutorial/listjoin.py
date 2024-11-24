# joining lists

lis1 = ["a", "b", "c"]
list2 = ["1", "2", "3"]

list3 = lis1 + list2

print(list3)

# we can also use loop to add

for x in list2:
 lis1.append(x)#append() is a function that adds values to the list from the end

print(lis1)

#we can also simply use extend() function which is used for adding elements from other list

numList = [1, 2, 3]
numList2 = [4, 5, 6]

numList.extend(numList2)

print(numList)

####################LIST METHODS#######################
#append()	 Adds an element at the end of the list
#clear()	  Removes all the elements from the list
#copy()	   Returns a copy of the list
#count()	  Returns the number of elements with the specified value
#extend()	 Add the elements of a list (or any iterable), to the end of the current list
#index()	  Returns the index of the first element with the specified value
#insert()	 Adds an element at the specified position
#pop()	    Removes the element at the specified position
#remove()	 Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	   Sorts the list