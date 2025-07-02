class Solution: 
    def twoSum(self, nums: list[int], target:int) -> list[int]:
        hashmap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n #hashmap method 
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return
