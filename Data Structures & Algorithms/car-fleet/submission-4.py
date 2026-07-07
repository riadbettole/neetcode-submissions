class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            arrival_time = (target - p) / s
            while stack and arrival_time <= stack[-1]:
                arrival_time = stack.pop() 
                
            stack.append(arrival_time)

        return len(stack)