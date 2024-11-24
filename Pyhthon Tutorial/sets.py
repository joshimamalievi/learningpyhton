#Set
#Sets are used to store multiple items in a single variable.

#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

#A set is a collection which is unordered, unchangeable*, and unindexed.

s = {1 , True , "abc"}
print(s)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:

#you can access elements and check if its in the set just like a list

#you can add items to set using add() function which adds without an order

s.add("Hello")

print(s)

#to add items from other set you use it update() function

s1 = {"bad", "crazy"}

s.update(s1)

print(s)

# you can add items from any iretable(lists, tuples, etc.)

l = [3, 2]

s.update(l)

print(s)

#to delete an item from a set you use remove()  or discard()

# the difference is that remove() method raises an error when there is no such item in the set

s.discard(1)
print(s)

#you can use also pop() to remove a random item

x = s.pop()

print(x)
print(s)

#clear() empties the set and del keyword deletes the entire set

del s

#looping is the same


#to join u need to use union() method to a new set which can be shorthanded like "|"

s2 = {"new", "set"}

sUn =s1.union(s2)

print(sUn)

s3 = {33, "yas"}

sUn2 = s1|s3

print(sUn2)

#multiple sets

sUn3 = s1.union(s2,s3)

print(sUn3) #heere we can use "|" aswell

sUnion = s1 | s2 | s3

print(sUnion)

#u can also add other data types like lists and tuples, u can add also using update() method which doesnt need a new set

#Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#ou can use the & operator instead of the intersection() method, and you will get the same result.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

#You can use the - operator instead of the difference() method, and you will get the same result.

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

############################METHODS##########################

#add()	 	Adds an element to the set
#lear()	 	Removes all the elements from the set
#opy()	 	Returns a copy of the set
#difference()	-	Returns a set containing the difference between two or more sets
#difference_update()	-=	Removes the items in this set that are also included in another, specified set
#discard()	 	Remove the specified item
#intersection()	&	Returns a set, that is the intersection of two other sets
#intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	 	Returns whether two sets have a intersection or not
#issubset()	<=	Returns whether another set contains this set or not
#<	Returns whether all items in this set is present in other, specified set(s)
#ssuperset()	>=	Returns whether this set contains another set or not
#>	Returns whether all items in other, specified set(s) is present in this set
#pop()	 	Removes an element from the set
#remove()	 	Removes the specified element
#symmetric_difference()	^	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
#union()	|	Return a set containing the union of sets
#update()	|=	Update the set with the union of this set and others