import hub
import time
import re

class CarController():
    def move(throttle, steer):
        # steerが0のとき、直進する
        if steer == 0:
            motor.run_at_speed(throttle)
            motor_steer.run_to_position(steer)
        # steerが0でないとき、角度steerだけ曲がる
        else:
            motor.run_at_speed(throttle)
            motor_steer.run_to_position(steer)

    def stop():
        motor.brake()
        motor_steer.brake()

    def straightening():
        once = False
        while True:
            difference_steer = int(-4*hub.motion.yaw_pitch_roll()[0]) #steer's value difinition by hub.motion.position
            if (difference_steer < -110):
                difference_steer = -110
            elif (difference_steer > 110):
                difference_steer = 110

            check = 0
            steer_speed = abs(difference_steer)
            if (steer_speed > 40):
                steer_speed = 40
            if (steer_speed < 8):
                steer_speed = 8

            if(motor_steer.busy(type=1)): #if motor_steer is moving
                continue
            elif once:
                break
            else:
                motor_steer.run_to_position(difference_steer)
                once = True

            if (motor_steer.get(2)[0] == 0):
                motor_steer.run_to_position(0)
                motor_steer.brake