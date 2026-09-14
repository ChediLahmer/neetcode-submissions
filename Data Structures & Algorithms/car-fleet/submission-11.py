class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        position, speed = map(list, zip(*sorted(zip(position, speed), reverse = True)))
        fleet_count = 1
        new_fleet = False
        if not position:
            return 0
        if len(position) == 1:
            return 1
        for idx in range(len(position)-1):
            step_1 = (target-position[idx])/speed[idx]
            step_2 = (target-position[idx+1])/speed[idx+1]
            if step_2 <= step_1:
              position[idx+1] = position[idx]
              speed[idx+1] = speed[idx]
              if not new_fleet:
                continue
              else:
                new_fleet = False
            else:
              new_fleet = True
              fleet_count +=1

        return fleet_count