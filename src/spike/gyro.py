from basic_motion import Basic_motion
import hub
class Gyro(Basic_motion):
    def __init__(self, motor_steer,motor,light_sensor):
        super().__init__(motor_steer,motor)
        self.destination=0
        self.differece_steer=0
        self.light_sensor=light_sensor


    def straightening(self,throttle,bias):
        self.difference_steer = int(
            -4 * (hub.motion.yaw_pitch_roll()[0] - (self.destination + bias)%360)
        )  # steer's value difinition by hub.motion.position
        if self.difference_steer < -110:
            self.difference_steer = -110
        elif self.difference_steer > 110:
            self.difference_steer = 110

        super().move(throttle,self.difference_steer)
        return 0;

    def change_steer(self):
        if(
        (abs(self.differece_steer)<=10) and #start up first
        (self.light_sensor.get(2)[0] > 0) and (self.light_sensor.get(2)[0] < 400) and
        (self.light_sensor.get(2)[1] > 100) and (self.light_sensor.get(2)[1] < 500) and
        (self.light_sensor.get(2)[2] > 300) and (self.light_sensor.get(2)[2] < 700) and
        (self.light_sensor.get(2)[3] > 400) and (self.light_sensor.get(2)[3] < 800)  ):  #if find blue(gabagaba)
            self.destination+=90
