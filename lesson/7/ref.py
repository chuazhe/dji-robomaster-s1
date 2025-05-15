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
ep_robot.chassis.move(x=1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=-1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=1,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=-1,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=0,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0,y=0,z=-90,xy_speed=0,z_speed=30).wait_for_completed()

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
#倒车入库
ep_robot.chassis.move(x=-0.9, y=0, z=0, xy_speed=0.5).wait_for_completed()

#前进入库
#ep_robot.chassis.move(x=0.9, y=0, z=0, xy_speed=0.5).wait_for_completed()

#左平移入库
#ep_robot.chassis.move(x=0, y=-0.4, z=0, xy_speed=0.5).wait_for_completed()

#右平移入库
#ep_robot.chassis.move(x=0, y=-0.4, z=0, xy_speed=0.5).wait_for_completed()


###结束机器人程序###
ep_robot.close()
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

"""侧方停车"""
ep_robot.chassis.move(x=0.6, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进

ep_robot.chassis.move(x=-0.3, y=0, z=0, xy_speed=0.7).wait_for_completed()#后退，方便转向

ep_robot.chassis.move(x=0, y=0, z=45, z_speed=45).wait_for_completed()#右转，让车身部分驶入车位

ep_robot.chassis.move(x=-0.6, y=0, z=0, xy_speed=0.7).wait_for_completed()#后退，全部进入停车位

ep_robot.chassis.move(x=0, y=0, z=-45, z_speed=45).wait_for_completed()#左转，车头摆正

ep_robot.chassis.move(x=-0.2, y=0, z=0, xy_speed=0.7).wait_for_completed()#后退，保证全部停入（可不加）


###结束机器人程序###
ep_robot.close()
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

val=0.5#val为迷宫一格长度

ep_robot.chassis.move(x=val*2, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进2格

ep_robot.chassis.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()#右转90°

ep_robot.chassis.move(x=val*3, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进3格


 #*****找到宝藏后可开启led灯*****

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进1格

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进1格

ep_robot.chassis.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()#右转90°

ep_robot.chassis.move(x=val, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进1格

ep_robot.chassis.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()#右转90°

ep_robot.chassis.move(x=val*2, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进2格

ep_robot.chassis.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()#右转90°

ep_robot.chassis.move(x=val, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进1格

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进1格

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val*2, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进1格



###结束机器人程序###
ep_robot.close()
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

val=0.5#val为迷宫一格长度

ep_robot.chassis.move(x=val*8, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进8格

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val*6, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进6格

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val*7, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进7格

ep_robot.chassis.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()#右转90°

ep_robot.chassis.move(x=val*7, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进7格

ep_robot.chassis.move(x=0, y=0, z=90, z_speed=45).wait_for_completed()#右转90°

ep_robot.chassis.move(x=val*9, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进9格

ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()#左转90°

ep_robot.chassis.move(x=val*3, y=0, z=0, xy_speed=0.7).wait_for_completed()#前进3格

###结束机器人程序###
ep_robot.close()
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
val_1=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_1, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_2=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_2, z_speed=45).wait_for_completed()

val_3=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_3, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_4=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_4, z_speed=45).wait_for_completed()

val_5=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_5, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_6=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_6, z_speed=45).wait_for_completed()

val_7=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_7, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_8=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_8, z_speed=45).wait_for_completed()

val_9=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_9, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_10=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_10, z_speed=45).wait_for_completed()

val_11=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_11, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_12=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_12, z_speed=45).wait_for_completed()

val_13=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_13, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_14=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_14, z_speed=45).wait_for_completed()

val_15=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_15, y=0, z=0, xy_speed=0.7).wait_for_completed()

val_16=int(input("请输入转向角度："))
ep_robot.chassis.move(x=0, y=0, z=val_16, z_speed=45).wait_for_completed()

val_17=int(input("请输入前进距离："))
ep_robot.chassis.move(x= val_17, y=0, z=0, xy_speed=0.7).wait_for_completed()

###结束机器人程序###
ep_robot.close()
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
ep_robot.chassis.move(x=1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=1,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=-1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=-1,z=0,xy_speed=1,z_speed=0).wait_for_completed()
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