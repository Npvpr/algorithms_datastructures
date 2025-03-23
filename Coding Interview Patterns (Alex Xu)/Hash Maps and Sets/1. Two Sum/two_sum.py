class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        old_nums = {}
        for index, value in enumerate(nums):
            required_value = target - value
            if required_value in old_nums:
                # keys are hashed(unique), so the values of the array are stored as keys in dictionary
                return [old_nums[required_value], index]
            else:
                old_nums[value] = index