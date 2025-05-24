# Lesson 2 Slide 25
print("Hello Python!")
print(99+67)

from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE, times=3)
time.sleep(2)

ep_robot.close()#导入编程操控机器人需要的模块
