p = "Hello India"
q = 10
r = 10.2
print(type(p))
print(type(q))
print(type(r))
print(type(12+31j))

###############

var = 13.2
print(type(var))
#13.2

type (var)
#<class ‘float’>

var = "Now the type is string"
print(type(var))

type(var)
#<class ‘str’>
var = 13.2
print(var)
#13.2

#############
print(type(bool(22)))
print(type(True))
print(type(False))
'''
Output:
<class 'bool'>
<class 'bool'>
<class 'bool'>
'''

bool(False)
print(bool(False))
#False
va1 = 0
print(bool(va1))
#False

va2 = 11
print(bool(va2))
#True

va3 = -2.3
print(bool(va3))
#True

#### Strings
str1 = 'Hello how are you'
str2 = "Hello how are you"
str3 = 'multiline'+'string';
print(str1)
print(str2)
print(str3)

f = 'data'
s = 'structure'
print(f + s)
#'datastructure'
print('Data ' + 'structure')
#Data structure


st = 'data.'
print(st * 3)
#'data.data.data.'
print(3 * st)
#'data.data.data.'

###### Range ######

print(list(range(10)))
print(range(10))
print(list(range(10)))
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(20,10,-2)))

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#range(0, 10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#range(1, 10, 2)
#[1, 3, 5, 7, 9]
#[20, 18, 16, 14, 12]


###### Lists ######

a = ['food', 'bus', 'apple', 'queen']
print(a)
#['food', 'bus', 'apple', 'queen']


mylist  = [10, "India", "world", 8] 
# accessing elements in list.
print(mylist[1])
#India



###### Ordered List ######

[10, 12, 31, 14] == [14, 10, 31, 12]
print([10, 12, 31, 14] == [14, 10, 31, 12])
#False


###### Dynamic List ######
b = ['data', 'and', 'book', 'structure', 'hello', 'st']

b += [32]
print(b)
#['data', 'and', 'book', 'structure', 'hello', 'st', 32]


b[2:3] = []
print(b)
#['data', 'and', 'structure', 'hello', 'st', 32]

del b[0]
print(b)
#['and', 'structure', 'hello', 'st', 32]

a = [2.2, 'python', 31, 14, 'data', False, 33.59]
print(a)
#[2.2, 'python', 31, 14, 'data', False, 33.59]


a = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print(a[0])
'data'
print(a[2])
'using'
print(a[-1])
'learning'
print(a[-5])
'structures'


print(a[1:5])
['structures', 'using']

print(a[-3:-1])
['python', 'happy']

######### Mutable ####
a = ['data', 'and', 'book', 'structure', 'hello', 'st']
print(a)
['data', 'and', 'book', 'structure', 'hello', 'st']
a[1] = 1
a[-1] = 120
print(a)
['data', 1, 'book', 'structure', 'hello', 120]

a = ['data', 'and', 'book', 'structure', 'hello', 'st']

print(a[2:5])
['book', 'structure', 'hello']
a[2:5] = [1, 2, 3, 4, 5]
print(a)
['data', 'and', 1, 2, 3, 4, 5, 'st']

######### Other operators ####

a = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print('data' in a)
#True

print(a)
#['data', 'structures', 'using', 'python', 'happy', 'learning']

a + ['New', 'elements']
print(a)
#['data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements']

print(a * 2)
#['data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements', 'data', 'structures', 'using', 'python', 'happy', 'learning', 'New', 'elements']

print(len(a))
#6
print(min(a))


############ Membership operators

#using 'in' operator
mylist1=[100,20,30,40]
mylist2=[10,50,60,90]
if mylist1[1] in mylist2:
    print("elements are overlapping")   	
else:
    print("elements are not overlapping")

#Output:
#elements are not overlapping 


########## Program to illustrate 'not in' operator
val = 104
mylist = [100, 210, 430, 840, 108]
if val not in mylist:
     print("val is NOT present in mylist")
else:
     print("val is  present in mylist")
 
#Output:
#val is NOT present in mylist



############# Example program to demonstrate the use of 'is' operator
Firstlist = []
Secondlist = []
if Firstlist == Secondlist:
   print("Both are equal")
else:
   print("Both are not equal")
if Firstlist is Secondlist:
   print("Both variables are pointing to the same object")
else:
   print("Both variables are not pointing to the same object")
thirdList = Firstlist
if thirdList is Secondlist:
   print("Both are pointing to the same object")
else:
   print("Both are not pointing to the same object") 
'''
Output:
Both are equal	
Both variables are not pointing to the same object
Both are pointing to the same object
'''



####### Example program to demonstrate the use of 'is not' operator
Firstlist = []
Secondlist = []
if Firstlist is not Secondlist:
  print("Both Firstlist and Secondlist variables are the same object")
else:
  print("Both Firstlist and Secondlist variables are not the same object") 

#Output:
# Both Firstlist and Secondlist variables are the same object



############## Logical Operators 

#### Example program to demonstrate the use of 'and' operator
a = 32
b = 132
if a > 0 and b > 0:
  print("Both a and b are greater than zero")
else:
  print("At least one variable is less than 0") 

#Output:
#Both a and b are greater than zero



######### Example program to demonstrate the use of 'or' operator
a = 32
b = -32
if a > 0 or b > 0:
  print("At least one variable is greater than zero")
else:
  print("Both variables are less than 0") 

#Output:
#At least one variable is greater than zero


########## Example program to demonstrate the use of 'or' operator
a = 32
if not a:
  print("Boolean value of a is False")
else:
  print("Boolean value of a is True") 

#Output:
#Boolean value of a is True




########## Tuple ###########

tupleName = ("entry1" , "entry2" , "entry3")
myTuple = ("Shyam", 23 , True , "male")
print(len((4,5, 'hello')))
  
print((4,5)+(10,20))
print((2,1)*3)
print(3 in ('hi', 'xyz',3))
for p in (6,7,8):  
    print(p)

x = ('hello', 'world', 'india')
print(x[1])
print(x[-2])
print(x[1:])


######### Dictionaries #########
my_dict = { 
     '1': 'Data',
     '2': 'Structure',
     '3': 'python',
     '4': 'programming',
     '5': 'language'
}


############

person = {}
print(type(person))
#<class 'dict'>

person['name'] = 'ABC'
person['lastname'] = 'XYZ'
person['age'] = 31
person['address'] = ['Jaipur']

print(person)
#{'name': 'ABC', 'lastname': 'XYZ', 'age': 31, 'address': ['Jaipur']}

print(person['name'])
#'ABC'


print('name' in person)
#True
print('fname' not in person)
#True 
print(len(person))
#4

mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict)
#{'a': 1, 'b': 2, 'c': 3}
mydict.clear()
print(mydict)
#{}

'''
mydict.get('b')
print(mydict)
#2
mydict.get('z')
print(mydict)
#None

print(list(mydict.items()))
#[('a', 1), ('b', 2), ('c', 3)]

print(list(mydict.keys()))
#['a', 'b', 'c']

print(list(mydict.values()))
#[1, 2, 3]

print(mydict.pop('b'))
#2
print(mydict)
#{'a': 1, 'c': 3}
mydict = {'a': 1,'b': 2,'c': 3}
print(mydict.popitem())
#('c', 3)
print(mydict)
#{'a': 1, 'b': 2}
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

print(d1.update(d2))
print(d1)
#{'a': 10, 'b': 200, 'c': 30, 'd': 400}
'''


############## SETS #############

x1 = set(['and', 'python', 'data', 'structure'])
print(x1)
#{'and', 'python', 'data', 'structure'}
print(type(x1))
#<class 'set'>

x2 = {'and', 'python', 'data', 'structure'}
print(x2)
#{'and', 'python', 'data', 'structure'}
x = {'data', 'structure', 'and', 'python'}
print(len(x))
#4
print('structure' in x)
#True
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

######### Union of two sets, x1 and x2. 
x3 = x1 | x2
print(x3)
{'java', 'structure', 'c', 'python', 'data'}

print(x1.union(x2))
{'java', 'structure', 'c', 'python', 'data'}


########## Intersection of sets
print(x1.intersection(x2))
#{'data'}
print(x1 & x2)
#{'data'}


########## Difference of sets

print(x1.difference(x2))
#{'structure'}
print(x1 - x2)
#{'structure'}


######### Symmetric difference ########## 
print(x1.symmetric_difference(x2))
#{'structure', 'python', 'c', 'java'}

print(x1 ^ x2)
#{'structure', 'python', 'c', 'java'}

####### subset ######

print(x1.issubset(x2))
#False
print(x1 <= x2)
#False

########## Immutable Sets #########

x = frozenset(['data', 'structure', 'and', 'python'])
print(x)
#frozenset({'and', 'python', 'data', 'structure'})
##### Error in the below code ####
'''
a11 = set(['data'])
a21 = set(['structure'])
a31 = set(['python'])
x1 = {a11, a21, a31}
'''

a1 = frozenset(['data'])
a2 = frozenset(['structure'])
a3 = frozenset(['python'])
x = {a1, a2, a3}
print(x)



######## Named Tuples ########

from collections import namedtuple
Book = namedtuple ('Book', ['name', 'ISBN', 'quantity'])
Book1 = Book('Hands on Data Structures', '9781788995573', '50')
# Accessing data items
print('Using index ISBN:' + Book1[1])
#Using index ISBN: 9781788995573
print('Using key ISBN:' + Book1.ISBN)
#Using key ISBN: 9781788995573


######## Deque ############

from collections import deque
s = deque()        # Creates an empty deque
print(s)
my_queue = deque([1, 2, 'Name'])
print(my_queue)
#deque([1, 2, 'Name'])
my_queue.append('age')
print(my_queue)
my_queue.appendleft('age')
print(my_queue)
my_queue.pop()
print(my_queue)
my_queue.popleft()
print(my_queue)


########## Ordered Dictionaries ########

from collections import OrderedDict
od = OrderedDict({'my': 2, 'name ': 4, 'is': 2, 'Mohan' :5})
od['hello'] = 4
print(od)
#([('my', 2), ('name', 4), ('is', 2), ('Mohan', 5), ('hello', 4)])


############ Default Dictionary ########

from collections import defaultdict
dd = defaultdict(int)
words = str.split('data python data data structure data python')
for word in words: 
   dd[word] +=1

print(dd)
#defaultdict(<type 'int'>, {'data': 4, 'python': 2, 'structure': 1})




############ ChainMap Object ##############

from collections import ChainMap
dict1 = {"data": 1, "structure": 2}
dict2 = {"python": 3, "language": 4}
chain = ChainMap(dict1, dict2)

print(chain)
#ChainMap({'data': 1, 'structure': 2}, {'python': 3, 'language': 4})
print(list(chain.keys()))
#['python', 'language', 'data', 'structure']
print(list(chain.values()))
#[3, 4, 1, 2]
print(chain["data"])
#1
print(chain["language"])
#4


################ Counter Objects ###########

from collections import Counter
inventory = Counter('hello')
print(inventory)
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})



############### UserDict #############
'''
from collections import UserDict  
class MyDict(UserDict):  
    def push(self, key, value):
        raise RuntimeError("Cannot insert")
        
d = MyDict({'ab':1, 'bc': 2, 'cd': 3})  
d.push('b', 2)

Traceback (most recent call last):
  File "<string>", line 12, in <module>
File "<string>", line 6, in push
RuntimeError: Cannot insert
'''

######### UserList ###########
'''
from collections import UserList  
class MyList(UserList):  
    def push(self, key):
       raise RuntimeError("Cannot insert in the list")
        
d = MyList([11, 12, 13])  
d.push(2)

Traceback (most recent call last):
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in push
RuntimeError: Cannot insert in the list
'''

######### UserString ##########

# create a custom append function for string
from collections import UserString
class MyString(UserString):  
    def append(self, value):
        self.data += value

s1 = MyString("data") 
print("Original:", s1)
#Original:  data

s1.append('h')
print("After append: ", s1)
#After append: datah



