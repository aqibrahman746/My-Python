"""
Lists, Tuples, Sets & Dictionaries
-----------
family = ["Aqib", "Samia", "Salma", "Khadija", "Ama", "Baba"]
otherFamily = ["Sasa", "Sasi", "Sumaya", "Eva"]
print(family)
print(family[3]) #Returns 'Khadija'
print(len(family)) #Returns length of list
print("Samia" in family) #Checks if item is in list

family[0] = "Bob" #Replaces Aqib with Bob
print(family) 
family[1:4] = ["Sarah", "Jeremiah", "Vanessa"] #Replaces Samia, Salma & Khadija
print(family)
family.insert(4, "Sasa") #Inserts an item into a list without replacement
print(family)

family.append("Sasi") #Adds item to list
print(family)
family.extend(otherFamily) #Adds other list onto current list
print(family)

family.remove("Aqib") #Removes specified item
print(family)

family.pop(2) #Removes item in specified index
print(family)

del family #del can also remove via index, but it can be used to delete the whole list
print(family)

family.clear() #Clears list, emptying contents
print(family)

for x in family: #Loops through list
    print(x)

for i in range(4): #Loops through list by index number. You can choose how many items to loop through
    print(family[i])

i = 0
while i < len(family):  #While loop version
    print(family[i])
    i = i+1

newFamily = [x for x in family if "b" in x] #List comprehension: shorter syntacx for when you want to create a new list based on values from an existing list.
print(newFamily) #Syntax: list = expression for item in iterable if condition == True
newFamily = [x for x in family if "m" not in x] #Returns items without m
print(newFamily)

family.sort() #Sorts list ascending
family.sort(reverse = True) #Descending sort
family.sort(key = str.lower) #Case-insensitive sort
family.reverse() #Reverse list order
print(family)

sameFamily = family.copy() #3 ways of copying lists
sameFamily = list(family)
sameFamily = family[:]
print(family)
print(sameFamily)

familyTuple = ("Aqib", "Samia", "Salma", "Khadija", "Ama", "Baba") #Tuples are unchangeable
print(familyTuple)

familySet = family = {"Aqib", "Samia", "Salma", "Khadija", "Ama", "Baba"} #Sets are unordered, unchangeable and unindexed. They do not allow duplicates.
print(familySet)

familyDict = { #Dictionaries are ordered and changeable, but they do not allow duplicates.
    "brother" : "Aqib",
    "sister_1" : "Salma",
    "sister_2" : "Samia",
    "sister_3": "Khadija",
    "mother": "Ama",
    "father": "Baba"
}
print(familyDict)
print(familyDict["brother"])
"""