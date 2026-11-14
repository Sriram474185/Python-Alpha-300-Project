mylist=["apple", "bananna", 'chery']
for i in mylist:
  print(i)
# mylist=list() where list() is a function
# to check weather a lement in the list 
if "chery" in mylist:
  print("Yes")
else :
  print("No")
mylist.append("lemon")
print(mylist)
mylist.insert(1,"berry")
print(mylist)
# pop() method removes the last element from the list
item = mylist.pop()
print("Removed item:", item)
# remove() method removes the  element from the list
mylist.remove("berry")
# clear () to clear 
# reverse() to reverse the list
# sort() to sort the list
#newlist=sorted(mylist) to sort the list and store in new list
a=mylist[0:2] #slicing the list
b=mylist.copy() #copying the list
# be very careful while copying the list using b=mylist as it will create a reference to the original list and any changes made to b will also affect mylist.
c=[1,2,3,4,5]
d=[i*i for i in c] #list comprehension
print(d)
#tuple is immutable and list is mutable
mytuple=("max",28,"male","max")
print(mytuple.count("max")) #count() method counts the number of occurrences of an element in the tuple
name,age,gender,name=mytuple #unpacking the tuple
print(name,age,gender)
#dictionary is a collection of key-value pairs
mydict={"name":"max","age":28,"gender":"male"}
print(mydict["name"]) #accessing the value using the key
mydict["age"]=29 #updating the value of a key
print(mydict)
mydict["city"]="new york" #adding a new key-value pair
print(mydict)
del mydict["city"] #deleting a key-value pair
print(mydict)
try:
  print(mydict["city"]) #this will raise a KeyError
except :
    print("KeyError: 'city' not found in the dictionary")
mydict2={"name":"Sriram","Age":21,"State":"Keralem"}
mydict.update(mydict2)
print(mydict)
print(mydict.keys())
print(mydict.values())
#set is a collection of unique elements ,mutable , no duplicates ,unordered
myset={1,2,3,4,5,5,5}
# .add() method adds an element to the set
myset.add(6)
print(myset)
myset.remove(3) #removes an element from the set
print(myset)
#.discard() method removes an element from the set if it is present, otherwise does nothing
myset.discard(10) #does nothing as 10 is not present in the set
#.clear() method removes all elements from the set
myset.clear()
#.union() method returns a new set with all elements from both sets
#.intersection() method returns a new set with elements that are common to both sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
#difference() method returns a new set with elements that are in the first set but not in the second set
print(set1.difference(set2))
#symmetric_difference() method returns a new set with elements that are in either of the sets but not in both
print(set1.symmetric_difference(set2))
#update() method updates the set with elements from another set
#set1.update(set2)
#issubset() method returns True if all elements of the set are present in another set
print(set1.issubset(set2))
#string is a collection of characters ,immutable
mystring="     Hello World     "
#.strip() method removes the leading and trailing whitespaces from the string
print(mystring.strip())
#.upper() , .lower() , .startwith() , .endswith() , .find() , .replace("old","new") , .split() , .join(),.count() methods are some of the commonly used string methods
#.split() method splits the string into a list of substrings based on a delimiter
# convertiong list to string using join() method
var=223
var1="ram"
str=f"your age is {var} and name is {var1}" #f-string
print(str)
# collections module provides alternatives to built-in types that can be more efficient and convenient for certain use cases
from collections import Counter
a="aaaaabbbbccddd"
mycounter=Counter(a)
print(mycounter)
print(mycounter.keys())
print(mycounter.values())
print(mycounter.items())
print(mycounter.most_common(2))
print(mycounter.most_common(1)[0][0]) #doubt
from collections import namedtuple
point = namedtuple('point','x,y')
pt=point(1,2)
print(pt)
print(pt.x,pt.y)
#itrtools module provides functions that create iterators for efficient looping
#lambda function is an anonymous function that can take any number of arguments but can only have one expression
#lambda arguments : expression
add10 =lambda x : x+10
print(add10(5))
print((lambda x,y: x*y)(5,6))
#random numbers 
import random
print(random.randint(1,10)) #returns a random integer between 1 and 10
print(random.random()) #returns a random float between 0 and 1
a=random.choice([1,2,3,4,5]) #returns a random element from the list
print(a)
b=random.sample([1,2,3,4,5],3) #returns a list of 3 random elements from the list
print(b)
#choices allows you to select multiple random elements from a list with replacement
c=random.choices([1,2,3,4,5],k=3)
print(c)
#suffle() method shuffles the elements of a list in place
mylist=[1,2,3,4,5]
random.shuffle(mylist)
print(mylist)

#dectorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it
def start_end_decorator(func):
  def wrapper():
    print("Start")
    func()
    print("End")
  return wrapper
@start_end_decorator
def print_name():
  print("Sriram")

print_name= start_end_decorator(print_name)
print_name()

#exceptio and error handling is a mechanism to handle runtime errors in a program
x=-5

"""if x<0:
  raise Exception("x' should be positive ")

assert(x>=0),'x is not  positive'
"""
"""
try:
  a=10/0
  b=a+4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("No exception occurred")
finally:
    print("This block will always be executed")

"""
#decorators
def my_decorators(func):
  def wrapper (*args,**kwargs):
    print("Before the function runs")
    result =func(*args,*kwargs)
    print("After the function runs")
    return result
  return wrapper

# Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example of a generator function is as follows:
def my_generator():
  yield 1
  yield 2
  yield 3

g=my_generator()
print(next(g))
print(next(g))

def countdown (num):
  print('Started')
  while num>0:
    yield num
    num -=1

cd=countdown(4)
print(next(cd))











