def majorityElement(nums):
        c=0
        candidate=0
        for num in nums:
            if c==0:
                candidate=num
                c+=1
            elif candidate==num:
                c+=1
            else:
                c-=1
        return candidate
nums=[2,2,1,1,1,2,2] 
print(majorityElement(nums))