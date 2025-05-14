
def singleNumber(nums: list[int]) -> int:
    data = {}
    if len(nums) == 1:
        return int(nums[0])
    else:
        for i in nums:
            data[f"{i}"] = nums.count(i)
        
        for key , value in data.items():
            if value == 1:
                return int(key)

    

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))