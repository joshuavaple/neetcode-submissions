class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach:
        Hash table = {item: index}
        For each item, take dif = target - item
        If dif was present in the hash table as a key, take the index
        If not, store this item, index in the hash table and continue
        The question assumption is there is exactly 1 pair (1 solution)
        Thus, there is no case of 2 repeated items that each is part of the solution
        E.g., [3, 4, 4, 5], target = 7, solutions = [0,1] and [0,2]
        """
        indices = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if indices.get(dif,None) != None:
                return [indices[dif], i]
            indices[nums[i]] = i # only update the hash after the check to avoid getting the same i when t=2*nums[i]



        

        