# Slide 
import robomaster
from robomaster import robot
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a=0
while a<2:
    ep_robot.chassis.move(x=0.2, y=0, z=0, xy_speed=a).wait_for_completed()
    time.sleep(0.1)
    a+=0.1
else:
    ep_robot.chassis.move(x=0.2, y=0, z=0, xy_speed=2).wait_for_completed()
    time.sleep(2)
    ep_robot.chassis.move(x=0, y=0, z=0, xy_speed=0).wait_for_completed()


###结束机器人程序###
ep_robot.close()








# Slide 
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a = 2.0
while a > 0:
    ep_robot.led.set_led(comp=led.COMP_ALL, r=255, g=255, b=0, effect=led.EFFECT_ON)
    ep_robot.chassis.move(x=0.7, y=0, z=0, xy_speed=a).wait_for_completed()
    # time.sleep(0.1)
    a -= 0.5

ep_robot.chassis.move(x=0, y=0, z=0, xy_speed=0).wait_for_completed()
time.sleep(2)
ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_ON)

###结束机器人程序###
ep_robot.close()








# Slide 
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a=0
while True:
    s = random.randint(1, 5)
    print(s)
    ep_robot.blaster.fire(times=s)
    a += s
    time.sleep(5)
    if a >= 15:
        break

###结束机器人程序###
ep_robot.close()
p=45
q=30
temp=p%q
while temp!=0:
    p=q
    q=temp
    temp=p%q
print(q)# 导入编程操控机器人需要的模块







# Slide 
import robomaster
from robomaster import robot
from robomaster import blaster
import time
import random

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a=1
p=int(input("第一个数:"))
q=int(input("第二个数:"))
temp=p%q
while temp!=0:
    p=q
    q=temp
    temp=p%q
print(q)
ep_robot.chassis.move(x=4, y=0, z=0, xy_speed=0.7).wait_for_completed()
while a<=q:
    ep_robot.blaster.fire(times=1)
    time.sleep(0.2)
    a+=1

###结束机器人程序###
ep_robot.close()









# Slide 
import robomaster
from robomaster import robot
from robomaster import blaster
import time
import random

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a=130
while a>0:
    ep_robot.gimbal.moveto(pitch=-5, yaw=a, pitch_speed=50, yaw_speed=100).wait_for_completed()
    ep_robot.blaster.fire(times=1)
    time.sleep(0.2)
    a-=40

###结束机器人程序###
ep_robot.close()






# Slide 
import robomaster
from robomaster import robot
from robomaster import blaster
import time
import random

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a = 30
while a < 160:
    ep_robot.chassis.move(x=0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_robot.gimbal.moveto(pitch=-5, yaw=a, pitch_speed=50, yaw_speed=100).wait_for_completed()
    ep_robot.blaster.fire(times=1)
    time.sleep(0.2)
    a += 40

###结束机器人程序###
ep_robot.close()








# Slide 
import robomaster
from robomaster import robot
from robomaster import blaster
import time
import random

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
a = 10
s=1
while a < 170:
    ep_robot.chassis.move(x=0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_robot.gimbal.moveto(pitch=-5, yaw=a, pitch_speed=50, yaw_speed=100).wait_for_completed()
    ep_robot.blaster.fire(times=1)
    if s==1:
        a += 30
    elif s==2:
        a+=50
    elif s==3:
        a+=50
    elif s>=4:
        a+=30
    s+=1
###结束机器人程序###
ep_robot.close()
