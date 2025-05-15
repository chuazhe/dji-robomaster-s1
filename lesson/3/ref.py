import time
print("绿灯亮15秒。")
time.sleep(15)
print("黄灯亮10秒。")
time.sleep(10)
print("红灯亮15秒。")
time.sleep(15)

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="breath")

###结束机器人程序###
ep_robot.close()

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="scrolling")

###结束机器人程序###
ep_robot.close()

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=0,g=255,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=0,g=0,b=255,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=0,g=0,b=255,effect="off")

###结束机器人程序###
ep_robot.close()
print("出发")
print("前进1000米")
print("向右转")
print("前进200米")
print("向左转")
print("前进500米")
print("到达超市")
print(123)
print(3.1415)
print(999+55)
print(999.0+55.0)
print(999+55.0)

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="on")
time.sleep(3)
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="off")

###结束机器人程序###
ep_robot.close()

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="bottom_front",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="bottom_left",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="bottom_back",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="bottom_right",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="top_left",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="top_right",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="off")

###结束机器人程序###
ep_robot.close()

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="bottom_all",r=0,g=0,b=255,effect="on")
ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="off")
time.sleep(2)
ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="off")
time.sleep(2)
ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="off")

###结束机器人程序###
ep_robot.close()

#导入编程操控机器人需要的模块
import robomaster
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
ep_robot.led.set_led(comp="bottom_front",r=255,g=0,b=0,effect="flash",freq=3)
time.sleep(1)
ep_robot.led.set_led(comp="bottom_front",r=255,g=0,b=0,effect="off")
ep_robot.led.set_led(comp="bottom_back",r=255,g=0,b=0,effect="flash",freq=3)
time.sleep(1)
ep_robot.led.set_led(comp="bottom_back",r=255,g=0,b=0,effect="off")
ep_robot.led.set_led(comp="bottom_left",r=255,g=0,b=0,effect="flash",freq=3)
time.sleep(1)
ep_robot.led.set_led(comp="bottom_left",r=255,g=0,b=0,effect="off")
ep_robot.led.set_led(comp="bottom_right",r=255,g=0,b=0,effect="flash",freq=2)
time.sleep(1)
ep_robot.led.set_led(comp="bottom_right",r=255,g=0,b=0,effect="off")

###结束机器人程序###
ep_robot.close()

#导入编程操控机器人需要的模块
import robomaster
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



###结束机器人程序###
ep_robot.close()