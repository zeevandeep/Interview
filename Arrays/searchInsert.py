def searchInsert(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	if not nums:
	    return 0
	for i in range(len(nums)):
	    #print i
	    if nums[i]==target:
	        
	        return i
	    elif nums[i] > target:
	    	if i ==0:
	    		
	    		return 0
	    	else:
	    		
	    		return i
	    	
	return i+1
	"""
	for i, element in enumerate(nums):
		if element >= target:
			return i
	return len(nums)
	"""
print searchInsert([1],0)