import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        for i in range(2):
            print(f'\033[31m {TrafficLight.__color[0]}')
            time.sleep(7)
            print(f'\033[33m {TrafficLight.__color[1]}')
            time.sleep(2)
            print(f'\033[32m {TrafficLight.__color[2]}')
            time.sleep(10)


traffic_light_model = TrafficLight()
traffic_light_model.running()

