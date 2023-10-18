print('Introduction to Python')
age= input('Enter ur fooking age: ')
print(age)

#For loop 
for index in range(5):
  print(index)

#For loop with step  
for index1 in range (0,11,12):
  print(index1) 
  
#Function 
def greet(name):
  print('hello' + name)  
greet('Mony')  
  
#List
fruit = ['apple','banana','coconut']
print(fruit[2])

fruit[1] = 'Watermelon'
fruit.append('dragon fruit')
#remove is used to remove by value
fruit.remove('dragon fruit')
#del is used to delete by index
# del fruit(0)
print(fruit)


#tuple works as list but can't modify (append or remove)
tuple = ('mony', 'jen', 'jcennie')
print(tuple[0]) 


#for loop
numbers = [1,2,3,4,5]
for index in numbers:
  print(index*2)

  
#for loop into new list  
newNumber = [1,2,3,4]
newList = []

for i in newNumber:
  newList.append(i*2)
print(newList)  



#for print only odd number 
comList = [1,2,3,4,5,6]
for i in comList: 
  i%2 == 0




#comprehension list 
newNumber1 = [1,2,3,4]
list=[i*2 for i in newNumber1]
print(list)

#comprehension even and odd 

# comList = [for ]
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

#retrieve 
new = my_dict.get("name")
print(new)

#modify, replace the old age to 19
my_dict["age"] = 19

#adding
my_dict['age'] = '29'
print(my_dict)

#del
del my_dict['city']
print(my_dict)