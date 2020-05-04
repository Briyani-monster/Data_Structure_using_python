#leet code question maximum array
#kadane Algorithms
nums=[-2,1,-3,4,-1,2,1,-5,4]
maxs=nums[0]
max_sofar=nums[0]
for i in range(1,len(nums)):
	max_sofar=max(nums[i],max_sofar+nums[i])
	if max_sofar>maxs:
		maxs=max_sofar
print(maxs)
