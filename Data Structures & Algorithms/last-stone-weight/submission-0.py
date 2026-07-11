class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [ -n for n in stones ]
        heapq.heapify(heap)

        while len(heap) > 1 :
            rock1, rock2 = heapq.heappop(heap), heapq.heappop(heap)

            if rock1 != rock2:
                new_stone = -abs(rock1 - rock2)
                heapq.heappush(heap, new_stone)
        
        return -heap[0] if heap else 0
