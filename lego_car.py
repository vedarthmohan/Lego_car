from hub import light_matrix
import motor
from hub import port, sound
import runloop
import force_sensor
import color_sensor, color

def stopCar():
    motor.stop(port.E)
    motor.stop(port.F)

async def main():
    running = False
    velocity = 0
    Fdegrees = -360
    Edegrees = 360
    while (True):
        if color_sensor.color(port.C) is color.RED:
            stopCar()
            running = False
        if color_sensor.color(port.C) is color.YELLOW:
            running = True
            velocity = 90
        if color_sensor.color(port.C) is color.GREEN:
            running = True
            velocity = 360        
        if (force_sensor.pressed(port.A)):
           motor.run_for_degrees(port.F, Edegrees, 360)
           motor.run_for_degrees(port.E, Fdegrees, 360)
        if (running == True):
            motor.run_for_degrees(port.F, Fdegrees, velocity)
            motor.run_for_degrees(port.E, Edegrees, velocity)

if __name__=="__main__":
    runloop.run(main())