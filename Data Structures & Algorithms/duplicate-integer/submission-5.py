class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            key = num
            if key in hash_map:
                
                return True
            else:
                hash_map[key] = num
        return False