import hub
import time
import re

hub.motion.preset_yaw(0)

print("--device init--")
while True:
    motor = hub.port.C.motor
    motor_steer = hub.port.E.motor

    ser = hub.port.D

    if ser==None or motor == None or motor_steer == None:
        continue
    motor.mode(2)
    ser.mode(hub.port.MODE_FULL_DUPLEX)
    motor_steer.mode(2)
    time.sleep(2)
    ser.baud(115200)
    time.sleep(1)
    break
"""
def move(throttle, steer):
    motor.run_to_position(1,1)
"""
def stop()
    motor.brake()
    motor_steer.brake()
thr = 3 #When stop return action
motor_steer.preset(0)# steer_motor run_to_position value reset

motor.run_at_speed(10)

motor_steer.run_to_position(20, 20)
#wait specific rotation
while motor.get(2)[0]<360:
    pass
motor_steer.run_to_position(0, 20)
print(hub.motion.position()[0])

while hub.motion.position()[0] > thr:
    motor_steer.run_at_speed(-10)
    print("in_yaw: {}".format(hub.motion.position()[0]))
motor_steer.run_to_position(0, 20)
print("post_yaw: {}".format(hub.motion.position()[0]))


'''
motor.run_for_degrees(720, 20)
while(motor_steer.get(2)[0] < 20):
    motor_steer.run_at_speed(10)

motor.run_for_degrees(720, 20)

while(motor_steer.get(2)[0] > -20):
    motor_steer.run_at_speed(-20)

motor.run_for_degrees(720,20)

while(motor_steer.get(2)[0] < 0):
    motor_steer.run_at_speed(20)

motor.brake()
motor_steer.brake()
'''
