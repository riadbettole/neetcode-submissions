class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, [(target - p) / s for p, s in zip(position, speed)]))
        stack = []

        for p, time in reversed(cars):
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)