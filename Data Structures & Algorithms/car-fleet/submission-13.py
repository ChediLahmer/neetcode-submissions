class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if not position:
            return 0
        cars = sorted(zip(position, speed), reverse = True)
        fleet_count = 0
        current_flee_time = 0.0
        
        for pos, spd in cars:
            time_to_target = ( target - pos ) / spd
            if time_to_target > current_flee_time:
                fleet_count +=1
                current_flee_time = time_to_target
        return fleet_count