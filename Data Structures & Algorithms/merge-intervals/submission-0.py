class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_added = output[-1]

            if start <= last_added[1]:
                output[-1][1] = max(last_added[1], end)
            else:
                output.append([start, end])

        return output