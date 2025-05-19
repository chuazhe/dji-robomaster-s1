# Slide 7_1
print("追踪目标航天器")
distance = int(input("输入距离目标航天器的距离："))
if distance <= 150:
    print("向目标航天器逼近")
else:
    print("继续追踪目标航天器")#导入编程操控机器人需要的模块

# Slide 7_2
distance = int(input("与目标航天器的相对角度："))
if distance == 0:
    print("成功对接")
else:
    print("航天器相撞")

# Slide 8
print(1>2)
print(1<2)

# Slide 9
num1 = int(input("输入一个数："))
num2 = int(input("输入一个数："))
if num1 > num2:
    print(num1)
else:
    print(num2)

# Slide 17
from robomaster import robot
from robomaster import blaster
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE, times=1)

###结束机器人程序###
ep_robot.close()

# Slide 18
from robomaster import robot
from robomaster import blaster
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
robot_num = int(input("输入机器人编号："))
if robot_num % 2 != 0:
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=3)
else:
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=255, b=0, effect=led.EFFECT_ON)
    time.sleep(2)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=255, b=0, effect=led.EFFECT_OFF)

###结束机器人程序###
ep_robot.close()

# Slide 19
from robomaster import robot
from robomaster import blaster
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
fire_times = int(input("输入要发射的次数："))
if fire_times < 10:
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=fire_times)
else:
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=10)


###结束机器人程序###
ep_robot.close()
