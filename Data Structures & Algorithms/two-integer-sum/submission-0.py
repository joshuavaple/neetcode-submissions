class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if indices.get(dif,None) != None:
                return [indices[dif], i]
            indices[nums[i]] = i # only update the hash after the check to avoid getting the same i when t=2*nums[i]



        

        