class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                product_list[i] *= nums[j]
        return product_list