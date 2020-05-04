def twosum(nums,target):	 
	 maps={}       
	        for i in range(len(nums)):
	            a=nums[i]
	            if a in maps:
	                  return [maps[a],i]
	                  break
	            else:
	                  e=target-nums[i]   
	                  maps[e]= i
	        return [maps[nums[i]],i]
twosum([1,2,3,4,5,6,7,8],3)	        
