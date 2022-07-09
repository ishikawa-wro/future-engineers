import hub
import time
import re

hub.motion.yaw_pitch_roll(0)

print("--device init--")
while True:
    motor = hub.port.C.motor
    motor_steer = hub.port.E.motor
    distance_sensor = hub.port.B.device
    light_sensor = hub.port.A.device
    port_a = hub.port.A

    ser = hub.port.D

    if ser == None or motor == None or motor_steer == None or distance_sensor == None or light_sensor == None:
        continue
    motor.mode(2)
    ser.mode(hub.port.MODE_FULL_DUPLEX)
    motor_steer.mode(2)
    light_sensor.mode(5)
    time.sleep(2)
    ser.baud(115200)
    time.sleep(1)
    break
"""
def move(throttle, steer):
    motor.run_to_position(1,1)
"""
def stop():
    motor.brake()
    motor_steer.brake()

thr = 3 #When stop return action
motor_steer.preset(0)# steer_motor run_to_position value reset

motor.run_at_speed(50)

motor_steer.run_to_position(110, 100, 100)

#wait specific rotation
while motor.get(2)[0]<180:
    pass
"""
motor_steer.run_to_position(0, 100)
print(hub.motion.yaw_pitch_roll()[0])
"""
def straightening():
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
        """
        while(motor_steer.get(2)[0] <= difference_steer):
            motor_steer.run_at_speed(steer_speed)
            check = 1

        while(motor_steer.get(2)[0] > difference_steer):
            motor_steer.run_at_speed(-steer_speed)
            check = 1
        """
        if(motor_steer.busy(type=1)): #if motor_steer is moving
            continue
        else:
            motor_steer.run_to_position(difference_steer)
        """
        if (check == 1):
            print(motor_steer.get(2)[0] , difference_steer)
            check = 0
        """

        #if (motor_steer.get(2)[0] == 0) and (difference_steer == 0):
        """
        if (motor_steer.get(2)[0] == 0):
            motor_steer.run_to_position(0)
            motor_steer.brake
            break
        """
        if(
        (first ==1) or #start up first
        (light_sensor.get(2)[0] > 0) and (light_sensor.get(2)[0] < 400) and
        (light_sensor.get(2)[1] > 100) and (light_sensor.get(2)[1] < 500) and
        (light_sensor.get(2)[2] > 300) and (light_sensor.get(2)[2] < 700) and
        (light_sensor.get(2)[3] > 400) and (light_sensor.get(2)[3] < 800)  ):
            motor_steer.run_to_position(0)
            motor_steer.brake
            break

first = 1 #first flag
gyro_preset = 0

while True:

    if(
    (first ==1) or #start up first
    (light_sensor.get(2)[0] > 0) and (light_sensor.get(2)[0] < 400) and
    (light_sensor.get(2)[1] > 100) and (light_sensor.get(2)[1] < 500) and
    (light_sensor.get(2)[2] > 300) and (light_sensor.get(2)[2] < 700) and
    (light_sensor.get(2)[3] > 400) and (light_sensor.get(2)[3] < 800)  ):  #if find blue(gabagaba)
        if(first != 1):
            gyro_preset = 1
        if(gyro_preset):
            hub.motion.yaw_pitch_roll(90)
            gyro_preset = 0
        straightening()
        first = 0

    #print("in_yaw: {}".format(hub.motion.position()[0]))
print("end")

#motor_steer.run_to_position(0, 100, 100)
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
# ここにコードを書いてね :-)
