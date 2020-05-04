def containsdublicate(nums):
	return True if len(set(nums)) < len(nums) else False
print(containsdublicate([1,2,3,4,5,5,6,6]))	