thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)

#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Dictionaries are written with curly brackets, and have keys and values:

print(thisdict["brand"]) # calling an item


#duplicate key values will override itself

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)

#Accesing to this data can be several ways 

#1:

me = {
    "name" : "Joshgun",
    "surname" : "Imamalievi",
    "age" : 21
}

name = me["name"]
#2
surname = me.get("surname")
#3
keyValues = me.keys()
#4 Adding a new value

me["height"] = 1.90

print(me)

print(name)
print(surname)
print(keyValues)

#5 

values = me.values()

print(values)

items = me.items()

print(items)

#updating data

me.update({"height": 1.87})
print(me)

#to add items we can also use update
#removing is with pop(item)|for selected item|, popitem()|for the lastitem| and del dict["item"]|for again a selected item|

#looping around keys and values

for x,y in me.items():
    print(x, y)

#copying is with copy() fmethod

myEvilTwin = me.copy()

print(myEvilTwin)

#also works with dict(dict)
mecopy = dict(me)

print(mecopy)


#with dictionaries you can make nested keys and values:

myFamily = {
    "favorite" : {
        "name" : "Joshgun",
        "age" : 21
    },
    "notsoFavorite" : {
        "name" : "Joshgun's Brother", 
        "age" : 22
    }
}


print(myFamily)

#or you can just create subdictionaries and one main dictionary, so after the key values you write the names of the dictionaries

favorite = {
    "name" : "Joshgun",
    "age" : 21
}
notsoFavorite = {
    "name" : "Joshgun's Brother", 
    "age" : 22
}

myEvilFamily = {
    "favorite" : favorite,
    "notsoFavorite" : notsoFavorite
}

print(myEvilFamily)

#this is how you acces items from nested dictionaries:

print(myEvilFamily["favorite"]["name"])

#looping through nested dictionaries

for x, obj in myFamily.items():
    print("\t", x ) 
    for y in obj:
        print("\t\t",  y + ' :', obj[y])

#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary