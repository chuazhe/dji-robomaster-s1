# Lesson 2 Slide 25
print("Hello Python!")
print(99+67)

#导入编程操控机器人需要的模块
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE, times=3)
time.sleep(2)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
