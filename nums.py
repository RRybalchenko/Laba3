def find_missing(nums):
    return [x for x in range(nums[0], nums[-1]+1) 
                               if x not in nums]
  
nums = [1, 2, 4]
print(find_missing(nums))
