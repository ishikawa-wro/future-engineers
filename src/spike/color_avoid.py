# ここにコードを書いてね :-)
import hub
import time
import re

time.sleep(1)

print("--device init--")
while True:
    # motor init
    motor = hub.port.C.motor
    motor_steer = hub.port.E.motor
    force_sensor = hub.port.F.device
    dist_sensor = hub.port.B.device

    ser = hub.port.D

    if ser==None or motor == None or motor_steer == None or force_sensor == None or dist_sensor== None:
        continue
    ser.mode(hub.port.MODE_FULL_DUPLEX)
    dist_sensor.mode(0)
    time.sleep(2)
    ser.baud(115200)
    time.sleep(1)
    break

def move(throttle, steer):
    # steerが0のとき、直進する
    if steer == 0:
        motor.run_at_speed(-throttle)
        motor_steer.run_to_position(steer,speed=10)
    # steerが0でないとき、角度steerだけ曲がる
    else:
        motor.run_at_speed(-throttle)
        motor_steer.run_to_position(steer,speed=10)
        return steer

def stop():
    motor.brake()
    motor_steer.brake()


if __name__ == "__main__":
    #シリアルポートに残っているデータを空にする
    while True:
        reply = ser.read(10000)
        print(reply)
        if reply == b"":
            break

    print("--waiting RasPi--")
    end_flag = False
    prev_steer = 0
    throttle = 0
    steer = 0
    flag = False

    while True:
        cmd = ""

        while True:
            #receive operations(throttle, steer)
            reply = ser.read(8 - len(cmd))
            reply = reply.decode("utf-8")
            cmd = cmd + reply

            if len(cmd) >= 8 and cmd[-1:] == "@":
                cmd_list = cmd.split("@")
                if len(cmd_list) != 2:
                    print(len(cmd_list))
                    cmd = ""
                    continue

                #"end"を受け取ったとき、終了する
                if cmd_list[0] == "end":
                    print(" -- end")
                    end_flag = True
                    break

                throttle = int(cmd_list[0].split(",")[0])
                steer = int(cmd_list[0].split(",")[1])

            #send distance
            distance = dist_sensor.get(2)[0]
            time.sleep(10/1000)
            print("Distance: {}[cm]".format(distance))
            if distance:
                ser.write("{:3d}@".format(distance))
            else:
                ser.write("{:3d}@".format(0))

            if flag:
                stop()
            time.sleep(1/1000)
            if force_sensor.get(0)[0] >= 50:
                flag = True
            time.sleep(1/1000)
            if flag and force_sensor.get(0)[0] >= 50:
                flag = False
            break

        move(throttle, steer)

        #"end"を受け取ったとき、停止して終了する
        if end_flag:
            stop()
            break
