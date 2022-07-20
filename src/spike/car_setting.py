import hub
import time
import re

class CarSetting():
    def setup():
        print("--setup start--")
        time.sleep(1)
        while True:
            distance_sensor = hub.port.B.device
            light_sensor = hub.port.A.device
            serial = hub.port.D
            motor_throttle = hub.port.F.motor
            motor_steering = hub.port.E.motor

            if (
                distance_sensor == None 
                or light_sensor == None 
                or serial == None 
                or motor_throttle == None 
                or motor_steering == None
            ):
                continue

            serial.mode(hub.port.MODE_FULL_DUPLEX)
            light_sensor.mode(5)
            motor_steering.mode(3)
            motor_throttle.mode(2)

            time.sleep(1)
            serial.baud(115200)
            break

        print("--setup finished--")

        hub.motion.yaw_pitch_roll(0)
        print("Set Yaw")
        motor_steering.preset(0)

    def resetSerialBuffer():
        while True:
            reply = ser.read(10000)
            print(reply)
            if reply == b"":
                break