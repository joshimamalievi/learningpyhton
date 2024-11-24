neurodivergent = ["Josh", "Martina", "Vusal"]
neurodivergent.insert(3, "Buket")
print(neurodivergent)# inserting item into a list to preferred location

neurodivergent.append("Khagan")# add item to the last index
print(neurodivergent)

aisec = ["Buket_Aisec", "Vusal_OG_Aisec", "Martina_Future_Aisec"]
neurodivergent.extend(aisec)# you can use every type of list
print(neurodivergent)
neurodivergent.append("Khagan")
neurodivergent.remove("Khagan")# if there is more than 2 occurancies of the same item it removes the first one
print(neurodivergent)
x = len(neurodivergent) - 1 
neurodivergent.pop(x) # pop removes the item in given index
print(neurodivergent)
neurodivergent.pop() # if no index then the last item is removed
print(neurodivergent)
#i = 0
#while i < len(neurodivergent):
 #print(neurodivergent[i])
 #i += 1 looping through the list

#for i in range(len(neurodivergent)):
 #print(neurodivergent[i]) this is with for

[print(i) for i in neurodivergent] # this is a short way

neurodivergent.clear() # deleting the whole items in the least
print(neurodivergent)

del neurodivergent # deleting the whole list as a var also 