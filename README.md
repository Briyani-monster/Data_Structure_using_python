# Data_Structure_using_python
This Repository is of Data Structure Implimentation using python

ARRAYS

Array can be simply created using  list in python :
----------------------------------------------------------------------------------------------------------------
a=['a','b','c','d']
#lookup
print(f'array after printing 3rd element: {a[2]}')#O(1)

#push
a.append('e')#O(1)
print(f'array after appended: {a}') 

#pop last item
a.pop()
a.pop()#O(1)
print(f"array after poped two item : {a}") 

#inserting
a.insert(0,'x')#O(n)
print(f'array after inserted string: {a}')

#insert at position
a.insert(2,'alein') #O(n)
print(f'array after inserted string at position : {a}')

#replace
a[2]='ravi' #O(n)
print(f'array after replacing string at position : {a}')

-----------------------------------------------------------------------------------------------------------------------------------

and we can also use array module to do so in python
In this Repository array.py file is Implementation of array using ctypes(which is a build in module) module of python, allowing you to use existing libraries in other languages by writing simple wrappers in Python itself. 

This dynamic array can perform almost all function 

append---adds a element at end of the element
insert---insert the item at any specified index
delete---deletes end element  of array
remove---delete item from the given index
length---returns length of array
print---prints all element of an array
replace---replaces the index value with item value
  

