import ctypes
class  DynamicArray(object):
	"""docstring for  Dynamic arr"""
	def __init__(self):
		self.n=0  #count actual element
		self.capacity=1    #Default Capacity (capacity is total no. of element it is capable of handling)
		self.A=self.make_array(self.capacity)

	def __len__(self):
		'''
		Returns number of elements in array
		'''	
		return self.n

	def __getitem__(self,k):
		'''
		Returns value k at index of array
		'''
		if not 0<=k<self.n:
			return IndexError('k is out of bound')	
		
		return self.A[k] # Retrieve from the array at index k

	def append(self,element):
		'''
		adds a element at lat of the element
		'''
		if self.n==self.capacity:
			#double capacity if not enough room
			self._resize(2*self.capacity)

		self.A[self.n]=element # Set self.n index to element
		self.n+=1#increasing the count by one

	def insert(self,item,index):
		"""
		this will insert the item at any specified index
		error : it'll show "index out of bound" error when u enter index out of the array length
		"""	
		if not 0<=index<self.n:
			return 'index out of bound: please enter correct index of array'
		if self.n==self.capacity:
			self._resize(2*self.capacity)
		for i in range(self.n-1,index-1,-1):
			self.A[i+1]=self.A[i]
		self.A[index]=item 
		self.n+=1
	def delete(self):
		""" 
		deletes end element  of array
		"""	
		if self.n==0:
			return 'Empty array deletion is not possible '
		self.A[self.n-1]=0
		self.n-=1
	def remove(self,index):
		"""
		delete item from the given index
		"""		
		if self.n==0:
			return 'cannot able to delete'
		if index<0 or index>=self.n: 
			return IndexError("Index out of bound....deletion not possible")         
          
		if index==self.n-1: 
			self.A[index]=0
			self.n-=1
			return

		for i in range(index,self.n-1): 
			self.A[i]=self.A[i+1]             
		
		self.A[self.n-1]=0
		self.n-=1	 	
					
	def _resize(self,new_capacity):
		"""
		resizes interval array to new capacity the array
		"""
		B=self.make_array(new_capacity) #new bigger array
		for k in range(self.n): #refrence all existing value
			B[k]=self.A[k]	
		self.A=B # Call A the new bigger array 
		self.capacity=new_capacity # Reset the capacity 

	def make_array(self,new_capacity):
		'''
		Returns a new array with new_cap capacity
		'''
		return (new_capacity*ctypes.py_object)()
	def length(self):
		print(f"\n{self.n}")
		return 	
	def print(self):
		"""
		printing all element of an array
		"""	
		print("-----------------")
		for i in range(0,self.n):
			
			print(f"index {i}: {self.A[i]}")
		print("-----------------")


array1=DynamicArray()
array1.append(3)
array1.append(25)
array1.append(9)
array1.print()
array1.delete()
array1.print()
array1.print()
array1.length()

		


		