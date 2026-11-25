class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for i in nums:
            nums_count[i] = nums_count.get(i,0) + 1
        heap = []
        for num,count in nums_count.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count,num in heap]