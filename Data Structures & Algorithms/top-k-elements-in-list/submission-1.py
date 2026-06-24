class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_k = defaultdict(int)
        
        for num in nums:
            num_k[num] += 1
        
     
        sorted_nums = sorted(num_k.keys(), key=lambda x: num_k[x], reverse = True)

        return sorted_nums[:k]