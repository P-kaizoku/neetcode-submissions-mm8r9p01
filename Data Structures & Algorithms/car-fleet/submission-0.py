class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car_sp = zip(position, speed)

        car_sp = sorted(car_sp, key=lambda x:x[0], reverse=True)

        car_fleet = []

        for pos, speed in car_sp:
            time = (target-pos)/speed
            if car_fleet:
                if time > car_fleet[-1]:
                    car_fleet.append(time)
            else:
                car_fleet.append(time)

        return len(car_fleet)    
