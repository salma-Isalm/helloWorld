# Data-type

#  text type : string
# number type : int , float , complex
# boolean type  : True , False
# Binary type : bytes , bytearray
# noneType : none
# sequence type : list  , tuple , range

# text-type
collageName = 'বাংলাদেশ সুইডেন পলিটেকনিক ইন্সটিটিউট '
print(collageName)
print(type(collageName))
# concate-function
firstName = 'salma'
lastName = 'islam'
print(firstName + ' ' + lastName)
print('my name is ' + firstName + ' ' + lastName)
# string Formating
num1 = 10
num2 = 20
print('The Summation is',  (num1 + num2))
print(f'the total number is{num1 + num2}')
userName = 'salma hoque'
Id = 20
print(f'my name is{userName}& my user id is{Id}')
# number type :
'''
1--int
2--float 
3--complex
'''
x = 30
y = 20.04
z = 123j

print(type(x))
print(type(y))
print(type(z))
# boolean type
x = 10
y = 10
# print(type(x>y))
print(x == y)

# binary type bytes
serialNo = [21, 32, 12, 31, 45, 56, 123, 245, 255]
b = bytes(serialNo)
print(type(b))
# print(type(serialNo))

# binary type bytearray
serialNo = [21, 32, 12, 31, 45, 56, 123, 245, 255]
b1 = bytearray(serialNo)
# print(type(b1))
print(b1[1])
# bytearray holo muteable ba poribotton kora jay
# replas kora hoilo
b1[1] = 200
print(b1[1])

# none type data
x = None
print(type(x))

# sequence type data (list) -----> mutable data
nameList = ['sahajada', 'sultana', 'nowsin', 'suyada', 'jasima', 'nuranu']
# print(type(nameList)
nameList[3] = 'sahamna'
print(nameList[3])


#  type data (tuple)------> immuteable data
nameOfFriend = ('sahajada', 'sultana', 'nowsin', 'suyada', 'jasima', 'nuranu')
listOfAge = (12, 34, 23, 21)
print(type(listOfAge))
print(type(nameOfFriend))

# sequance type data (range)

ran = range(6)
for i in ran:
    print(i)
