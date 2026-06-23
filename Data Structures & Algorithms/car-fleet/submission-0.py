class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            # form a new fleet if its takes longer (>)
            if not stack or time > stack[-1]:
                stack.append(time)
            # otherwise it catches up to the fleet (merges) so do nothing 
        
        return len(stack)        