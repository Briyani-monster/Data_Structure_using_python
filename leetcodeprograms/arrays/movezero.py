def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if(n==0 or n==1):
            return (nums)
        left,right=0,0
        temp=0
        #Rearrangement
        while(right < n):
            if(nums[right]==0):
                right+=1
            else:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left+=1
                right+=1
        return (nums)    
nums=[0,1,0,3,12]
nums2=[0,0,1] 
print(moveZeroes(nums))
print(moveZeroes(nums2))       