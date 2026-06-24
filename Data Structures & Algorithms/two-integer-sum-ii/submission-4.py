class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        stored = {}

        for i in range(len(numbers)):
            if numbers[i] in stored:
                continue

            if target - numbers[i] in stored:
                return [stored[target - numbers[i]], i + 1]

            stored[numbers[i]] = i + 1
        
            