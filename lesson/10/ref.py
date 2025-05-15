print("追踪目标航天器")
distance = int(input("输入距离目标航天器的距离："))
if distance <= 150:
    print("向目标航天器逼近")
else:
    print("继续追踪目标航天器")#导入编程操控机器人需要的模块
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
pos_num = int(input("输入目标位置提示信息（1-4）："))
if pos_num == 1:
    ep_robot.chassis.move(x=0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
if pos_num == 2:
    ep_robot.chassis.move(x=-0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_robot.gimbal.moveto(pitch=0, yaw=180, pitch_speed=50, yaw_speed=200).wait_for_completed()
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
if pos_num == 3:
    ep_robot.chassis.move(x=0, y=-0.5, z=0, xy_speed=0.7).wait_for_completed()
    ep_robot.gimbal.moveto(pitch=0, yaw=-90, pitch_speed=50, yaw_speed=200).wait_for_completed()
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
if pos_num == 4:
    ep_robot.chassis.move(x=0, y=0.5, z=0, xy_speed=0.7).wait_for_completed()
    ep_robot.gimbal.moveto(pitch=0, yaw=90, pitch_speed=50, yaw_speed=200).wait_for_completed()
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
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
ep_robot.close()distance = int(input("与目标航天器的相对角度："))
if distance == 0:
    print("成功对接")
else:
    print("航天器相撞")print(1>2)
print(1<2)num1 = int(input("输入一个数："))
num2 = int(input("输入一个数："))
if num1 > num2:
    print(num1)
else:
    print(num2)#导入编程操控机器人需要的模块
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
ep_robot.close()#导入编程操控机器人需要的模块
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
bullet_type = input("输入发射类型：")
fire_times = int(input("输入发射的次数："))
if bullet_type == "w":
    ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=fire_times)
if bullet_type == "i":
    ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE, times=fire_times)


###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
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
ep_robot.close()#导入编程操控机器人需要的模块
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
base_life = int(input("输入敌方基地的生命值："))
if base_life == 0:
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_ON)
    time.sleep(0.5)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_OFF)
    time.sleep(0.5)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_ON)
    time.sleep(0.5)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_OFF)
    time.sleep(0.5)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_ON)
    time.sleep(0.5)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_OFF)
    time.sleep(0.5)
else:
    ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE, times=3)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
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
n1 = int(input("输入敌方基地生命值数值1："))
n2 = int(input("输入敌方基地生命值数值2："))
n3 = int(input("输入敌方基地生命值数值3："))
n_max = 0
if n1 > n2:
    n_max = n1
else:
    n_max = n2
if n_max < n3:
    n_max = n3
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=n_max)


###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
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