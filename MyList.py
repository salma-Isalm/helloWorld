li = [2, 3, 40, ]
print(type(li))
print(li)
# change list item
li[2] = 100
print(li)

# (insert) add item on list, it,s used  User Wishes
list = ['sumiya', 'nihal', 'homiyra', 'Labli', 'josna', 'sabrina', 'promi', 'rudra']
list.insert(2, 'bela')
print(list)
print(list[3:6])
List = [True, False, True, False, True]
# Access list data

print(List[2])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])

# (Append) Add item on  List
FriendAge = [23, 24, 21, 25, 21]
FriendAge.append(32)
print(FriendAge)
# (remove) Remove item on list
identity = ['sahana', 2002, True, 'MadeEasy']
identity.remove(2002)
print(identity)
identity.pop()
print(identity)
identity.pop(1)
print(identity)
friendAge = [23, 24, 21, 25, 21]
del friendAge[2]
print(friendAge)
friendAge.clear()
print(friendAge)
# Looping list item
# You can loop through the list items by using a for loop:

MyTotalFriendId = [210, 230, 140, 250, 180,170,]
for i in MyTotalFriendId:
     print(i)
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
for i in range(len(MyTotalFriendId)):
    print(i)
# Print all items, using a while loop to go through all the index numbers

i= 0
while i < len(MyTotalFriendId):
    print(MyTotalFriendId[i])
    i += 1

# List Comprehension
num = [2, 4, 5, 6, 8 ]
double = [i*2 for i in num]
print(double)
Number = [5, 3, 7, 4, 1, 0, 9]
# Number.sort()
# print(Number)
Number.sort(reverse= True)
print(Number)
Department = ['computer', 'mechanical', 'electrical', 'automobile', 'constraction']
# Department.sort()
# print(Department)
Department.reverse()
print(Department)
# Department.sort(reverse=True)
# print(Department)

#python Copy a List {copy()} ,
# num2 = num.copy()
# print(num)
# print(num2)

# Python - Join Lists

n1 = ["a", "b ",5]
n2 = [3, 6, 8]
n3 = n1+n2
print(n3)
n1.extend(n2)
print(n1)


