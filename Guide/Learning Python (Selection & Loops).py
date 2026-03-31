"""
#Selection
#----------------
a = 87
b = 46
smaller = a if a < b else b  #If and else statements can be one line. This can be used for variables. Here, smaller will be a if a < b, else it will be b.
print(smaller)
if b < 50:
    print("Smaller than 50")
    if b % 2 == 0:  #If statements can be nested
        print("And also a multiple of 2")
    else:
        print("But not a multiple of 2")

month = 4
match month:  #match evaluates its expression once and compares it to each of it's cases. The case that's true is the code that gets executed.
    case 12|1|2:
        print("It's Winter")
    case 3|4|5:
        print("It's Spring")
    case 6|7|8:
        print("It's Summer")
    case 9|10|11:
        print("It's Autumn")
"""
"""
Loops
--------------
i = 0
while i <= 5:  #While loops loop a statement as long as  the condition is true. Increments prevent an infinite loop.
    print("While loop")
    if i == 2:
        break  #break stops the loop even when the condition is true
    i = i + 1

i = 0
while i < 5:
    i += 1
    if i == 2:
        continue  #continue stops the current iteration and moves onto the next.
    print(i)

names = ["Bob", "Sarah", "Tony"]
for x in names:  #For loops iterate through a sequence
    print(x)

for i in range(0, 20, 5):  #The range function allows us to loop through a block of code a specified number of times. range(start, end, increment)
    print(i)

names = ["Bob", "Sarah" ,"Tony"]
class_ = ["1A", "5B", "8E"]

for i in names:
    for j in class_:  #For loops can be nested like so
        print(i, j)
"""
#Functions
#-----------------
def age_check():
    if age < 10:
        return "Too young"
    elif age > 50:
        return "Too old"
    else:
        return "Acceptable"
    
age = 30
print(age_check())