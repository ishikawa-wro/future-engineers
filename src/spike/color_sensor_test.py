import hub
import time
import re

hub.motion.preset_yaw(0)

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

light_sensor.mode(5)
port_a = hub.port.A
"""
for mode in port_a.info()["modes"]:
    print(mode)
    print("\n")
"""
motor.run_at_speed(20)
while True:
    time.sleep(2)
    print(light_sensor.get(2))
    #print(light_sensor.get(2)[0])

    if( (light_sensor.get(2)[0] > 100) and (light_sensor.get(2)[0] < 300) and
    (light_sensor.get(2)[1] > 200) and (light_sensor.get(2)[1] < 400) and
    (light_sensor.get(2)[2] > 400) and (light_sensor.get(2)[2] < 600) and
    (light_sensor.get(2)[3] > 500) and (light_sensor.get(2)[3] < 700) ):
        print("aoi")



