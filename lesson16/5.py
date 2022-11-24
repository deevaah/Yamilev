from time import sleep

class light:
    def __init__(self, light):
        self.light = light

    def red(self):
        sleep(1)
        print("red light")
    def yellow(self):
        sleep(0.5)
        print("yellow light")
    def green(self):
        sleep(2)
        print("green light")
traffic_r = light("red_light")
traffic_y = light("yellow_light")
traffic_g = light("green_light")

traffic_r.red()
traffic_y.yellow()
traffic_g.green()