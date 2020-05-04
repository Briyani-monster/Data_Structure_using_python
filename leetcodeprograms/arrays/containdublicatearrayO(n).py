def containsdublicate(nums):
  maps=[]
  for i in range(len(nums)):
    if nums[i] in maps:
      return 'true'
    else:
      maps.append(nums[i])
  return 'false'
print(containsdublicate([1,2,3,4,5,6,7,7]))  