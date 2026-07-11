class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [ -n for n in stones ]
        heapq.heapify(heap)

        while len(heap) > 1 :
            rock1 = heapq.heappop(heap)
            rock2 = heapq.heappop(heap)

            if rock2 > rock1:
                heapq.heappush(heap, rock1 - rock2)
        
        heap.append(0)
        return abs(heap[0])
