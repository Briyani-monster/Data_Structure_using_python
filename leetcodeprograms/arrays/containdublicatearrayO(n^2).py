def containsdublicate(nums):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      # print(nums[i],nums[j])
      if nums[i]==nums[j]:
        temp='true'
        return temp
      else:
        temp='false'
        continue
  return temp      
print(containsdublicate([1,2,3,4,5,6]))        
