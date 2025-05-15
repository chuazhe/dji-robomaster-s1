#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=-1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=0,z=90,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=0,z=-90,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=0,z=0,timeout=5)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.chassis.drive_speed(x=1,y=1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=-1,y=-1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=-1,y=1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=1,y=-1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=0,z=0,timeout=5)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=-1,y=0,z=0,timeout=5)
time.sleep(0.5)
ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
time.sleep(0.5)
ep_robot.chassis.drive_speed(x=-1,y=0,z=0,timeout=5)
time.sleep(0.5)
ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
time.sleep(0.5)
ep_robot.chassis.drive_speed(x=0,y=0,z=0,timeout=5)
###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
ep_robot.led.set_led(comp="bottom_front",r=0,g=255,b=0,effect="on")
time.sleep(1)
ep_robot.led.set_led(comp="bottom_front",r=0,g=255,b=0,effect="off")

ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
ep_robot.led.set_led(comp="bottom_left",r=0,g=255,b=0,effect="on")
time.sleep(1)
ep_robot.led.set_led(comp="bottom_left",r=0,g=255,b=0,effect="off")

ep_robot.chassis.drive_speed(x=-1,y=0,z=0,timeout=5)
ep_robot.led.set_led(comp="bottom_back",r=0,g=255,b=0,effect="on")
time.sleep(0.5)
ep_robot.led.set_led(comp="bottom_back",r=0,g=255,b=0,effect="off")

ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
ep_robot.led.set_led(comp="bottom_left",r=0,g=255,b=0,effect="on")
time.sleep(0.5)
ep_robot.led.set_led(comp="bottom_left",r=0,g=255,b=0,effect="off")

ep_robot.chassis.drive_speed(x=-1,y=0,z=0,timeout=5)
ep_robot.led.set_led(comp="bottom_back",r=0,g=255,b=0,effect="on")
time.sleep(0.5)
ep_robot.led.set_led(comp="bottom_back",r=0,g=255,b=0,effect="off")

ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
ep_robot.led.set_led(comp="bottom_left",r=0,g=255,b=0,effect="on")
time.sleep(0.5)
ep_robot.led.set_led(comp="bottom_left",r=0,g=255,b=0,effect="off")
ep_robot.chassis.drive_speed(x=0,y=0,z=0,timeout=5)
###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(0.5)
ep_robot.chassis.drive_speed(x=0,y=1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(0.5)
ep_robot.chassis.drive_speed(x=0,y=0,z=0,timeout=5)
ep_robot.play_sound(robot.SOUND_ID_SHOOT).wait_for_completed()

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###


###结束机器人程序###
ep_robot.close()