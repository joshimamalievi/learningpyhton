for x in range(2, 6): #The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
    print(x)
print("=======================================================================================================")
for x in range(2, 30, 3): #range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
    print(x)

print("=======================================================================================================")
#Breaking
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
print("=======================================================================================================")
#nested loops 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)