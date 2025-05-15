# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-1
   Description :
   Author :       mongo
   date：          2020/8/12
-------------------------------------------------
   Change Activity:
                   2020/8/12:
-------------------------------------------------
"""
import math

num = int(input("请输入一个整数"))
num_sqr = math.sqrt(num)
num_list = []
if num_sqr % 1 == 0:
    print(num,"的平方根是",num_sqr)
else:
    print(num,"没有整数平方根")
for i in range(1,1001):
    if math.sqrt(i) % 1 == 0:
        num_list.append(i)
print(num_list)

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-2
   Description :
   Author :       mongo
   date：          2020/8/12
-------------------------------------------------
   Change Activity:
                   2020/8/12:
-------------------------------------------------
"""
"""
cosA=(b²+c²-a²)/(2bc)
cosB=(a²+c²-b²)/(2ac)
cosC=(a²+b²-c²)/(2ab)

sinA = sqrt(1-cosB**2)
"""

import math

print("请输入三条边")
a = int(input(""))
b = int(input(""))
c = int(input(""))
if a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
else:
    print("不能构成三角形")
t_ac =(b**2+c**2-a**2)/(2*b*c)
t_bc =(a**2+c**2-b**2)/(2*a*c)
t_cc =(a**2+b**2-c**2)/(2*a*b)
t_as = math.sqrt((1-t_ac**2))
t_bs = math.sqrt((1-t_bc**2))
t_cs = math.sqrt((1-t_cc**2))
print("第一个角度的正弦是%f,余弦是%f"%(t_as,t_ac))
print("第二个角度的正弦是%f,余弦是%f"%(t_bs,t_bc))
print("第三个角度的正弦是%f,余弦是%f"%(t_cs,t_cc))
sin_45 = math.sin(math.radians(45))
cos_45 = math.cos(math.radians(45))
sin_60 = math.sin(math.radians(60))
cos_60 = math.cos(math.radians(60))
sin_90 = math.sin(math.radians(90))
cos_90 = math.cos(math.radians(90))
print("sin(45)=%f"%sin_45)
print("cos(45)=%f"%cos_45)
print("sin(60)=%f"%sin_60)
print("cos(60)=%f"%cos_60)
print("sin(90)=%f"%sin_90)
print("cos(90)=%f"%cos_90)# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-3
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
ep_robot.close()# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-4
   Description :
   Author :       mongo
   date：          2020/8/12
-------------------------------------------------
   Change Activity:
                   2020/8/12:
-------------------------------------------------
"""
'''
L = 20m
V外 = (R+L/2)/R * V=V + (L/2)*V/R
V内 = (R-L/2)/R * V=V - (L/2)*V/R
麦轮速度w，以车头方向前进旋转为正，
数值范围：-1000~1000（rpm，即每分钟的圈
数）w为50时较为安全，w为100时较快
公式里R为走圆周运动的半径，V代表drive_wheels里的w
drive_wheels方法里的w必须为整数，60.0在它里面不算整数，必须时60才行
所以给结果的时候强制整型转换
w1和w4为右侧轮子，w2和w3为左侧轮子，右侧轮子快往左绕圆，反之右绕圆
'''
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