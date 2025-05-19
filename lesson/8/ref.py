# Slide 21
import math
num = int(input("请输入一个整数"))
num_sqr = math.sqrt(num)


# Slide 24
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")
ep_chassis = ep_robot.chassis
###你要写的程序###

# 指定麦轮速度
speed = 50
slp = 1

# 前进 3秒
ep_chassis.drive_wheels(w1=speed, w2=speed, w3=speed, w4=speed)
time.sleep(slp)

# 后退 3秒
ep_chassis.drive_wheels(w1=-speed, w2=-speed, w3=-speed, w4=-speed)
time.sleep(slp)

# 左移 3秒
ep_chassis.drive_wheels(w1=speed, w2=-speed, w3=speed, w4=-speed)
time.sleep(slp)

# 右移 3秒
ep_chassis.drive_wheels(w1=-speed, w2=speed, w3=-speed, w4=speed)
time.sleep(slp)

# 左转 3秒
ep_chassis.drive_wheels(w1=speed, w2=-speed, w3=-speed, w4=speed)
time.sleep(slp)

# 右转 3秒
ep_chassis.drive_wheels(w1=-speed, w2=speed, w3=speed, w4=-speed)
time.sleep(slp)

# 停止麦轮运动
ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)

###结束机器人程序###
ep_robot.close()


# May not be used 
import robomaster
from robomaster import robot
from robomaster import led
import time
#help(robot.chassis)
###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_chassis = ep_robot.chassis
def speed(r,w):
    w_1 = w + (10) * w / r
    w_2 = w - (10) * w / r
    return [int(w_1),int(w_2)]
r = int(input("请输入走圆周运动的半径："))
w = int(input("请输入机器人的速度："))
v = speed(r,w)
print(v)
# flag = input("请选择朝左绕圆吗？y/n")
# if flag == 'y' or flag == 'Y':
#     ep_chassis.drive_wheels(w1=v[0], w2=v[1], w3=v[1],w4=v[0])
#     time.sleep(22)
#     ep_chassis.drive_wheels(w1=0, w2=0, w3=0,w4=0)
#     time.sleep(10)
# elif flag == 'n' or flag == 'N':
#     ep_chassis.drive_wheels(w1=v[1], w2=v[0], w3=v[0], w4=v[1])
#     time.sleep(20)
#     ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)
#     time.sleep(10)
###结束机器人程序###
# ep_robot.close()# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-5
   Description :
   Author :       mongo
   date：          2020/8/12
-------------------------------------------------
   Change Activity:
                   2020/8/12:
-------------------------------------------------
"""
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_chassis = ep_robot.chassis
ep_led = ep_robot.led
ep_led.set_led(comp='all', r=255, g=0, b=0,effect='on', freq=1)
ep_chassis.move(x=1, y=0, z=0, xy_speed=1,z_speed=0).wait_for_completed()
ep_chassis.move(x=0, y=0, z=90, xy_speed=0,z_speed=90).wait_for_completed()
ep_chassis.move(x=1, y=0, z=0, xy_speed=1,z_speed=0).wait_for_completed()
ep_chassis.move(x=0, y=0, z=90, xy_speed=0,z_speed=90).wait_for_completed()
ep_chassis.move(x=1, y=0, z=0, xy_speed=1,z_speed=0).wait_for_completed()
ep_chassis.move(x=0, y=0, z=90, xy_speed=0,z_speed=90).wait_for_completed()
ep_chassis.move(x=1, y=0, z=0, xy_speed=1,z_speed=0).wait_for_completed()
ep_led.set_led(comp='all', r=255, g=0, b=0,effect='off', freq=1)

ep_led.set_led(comp='all', r=0, g=255, b=0,effect='on', freq=1)
ep_chassis.drive_wheels(w1=105, w2=35, w3=35,w4=105)
time.sleep(7)
ep_chassis.drive_wheels(w1=0, w2=0, w3=0,w4=0)
time.sleep(2)
ep_led.set_led(comp='all', r=0, g=255, b=0,effect='off', freq=1)
###结束机器人程序###
ep_robot.close()# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-6
   Description :
   Author :       mongo
   date：          2020/8/12
-------------------------------------------------
   Change Activity:
                   2020/8/12:
-------------------------------------------------
"""
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_chassis = ep_robot.chassis
ep_chassis.drive_wheels(w1=100, w2=0, w3=0,w4=100)
time.sleep(3)
# ep_chassis.drive_wheels(w1=0, w2=0, w3=0,w4=0)
# time.sleep(10)
ep_chassis.drive_wheels(w1=0, w2=100, w3=100,w4=0)
time.sleep(3)
ep_chassis.drive_wheels(w1=0, w2=0, w3=0,w4=0)
time.sleep(10)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###


###结束机器人程序###
ep_robot.close()
