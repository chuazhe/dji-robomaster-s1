# Slide 23_1
#导入编程操控机器人需要的模块
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
ep_robot.gimbal.move(pitch=0, yaw=50, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.gimbal.move(pitch=10, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.gimbal.move(pitch=0, yaw=-100, pitch_speed=100, yaw_speed=100).wait_for_completed()



###结束机器人程序###
ep_robot.close()

# Slide 23_2
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
ep_robot.gimbal.move(pitch=0, yaw=20, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=20, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)

###结束机器人程序###
ep_robot.close()



# Slide 26_1
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
ep_robot.gimbal.moveto(pitch=0, yaw=50, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.gimbal.moveto(pitch=0, yaw=-50, pitch_speed=100, yaw_speed=100).wait_for_completed()


###结束机器人程序###
ep_robot.close()



# Slide 26_2
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
ep_robot.gimbal.moveto(pitch=0, yaw=30, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.moveto(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.moveto(pitch=0, yaw=-30, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.moveto(pitch=0, yaw=-60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.moveto(pitch=0, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)


###结束机器人程序###
ep_robot.close()


# Slide 27
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
ep_robot.gimbal.move(pitch=0, yaw=-110, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)
time.sleep(1)
ep_robot.gimbal.move(pitch=0, yaw=60, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.blaster.fire(fire_type=blaster.WATER_FIRE, times=1)

###结束机器人程序###
ep_robot.close()


# Slide 28
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
ep_robot.gimbal.drive_speed(pitch_speed=0, yaw_speed=100)
time.sleep(1)
ep_robot.gimbal.drive_speed(pitch_speed=0, yaw_speed=-100)
time.sleep(1)
ep_robot.gimbal.drive_speed(pitch_speed=15, yaw_speed=0)
time.sleep(1)
ep_robot.gimbal.drive_speed(pitch_speed=-15, yaw_speed=0)
time.sleep(1)
ep_robot.gimbal.drive_speed(pitch_speed=0, yaw_speed=0)


###结束机器人程序###
ep_robot.close()


# Slide 27
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
ep_robot.gimbal.drive_speed(pitch_speed=0, yaw_speed=100)
time.sleep(2)
ep_robot.gimbal.recenter(pitch_speed=0, yaw_speed=100)


###结束机器人程序###
ep_robot.close()


# Maybe no used 
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
#口
ep_robot.gimbal.moveto(pitch=20, yaw=-20, pitch_speed=80, yaw_speed=80).wait_for_completed()
ep_robot.gimbal.moveto(pitch=-20, yaw=-20, pitch_speed=80, yaw_speed=80).wait_for_completed()
ep_robot.gimbal.moveto(pitch=-20, yaw=20, pitch_speed=40, yaw_speed=40).wait_for_completed()
ep_robot.gimbal.moveto(pitch=20, yaw=20, pitch_speed=40, yaw_speed=40).wait_for_completed()
ep_robot.gimbal.moveto(pitch=20, yaw=-20, pitch_speed=80, yaw_speed=80).wait_for_completed()

#V
ep_robot.gimbal.moveto(pitch=20, yaw=-20, pitch_speed=80, yaw_speed=40).wait_for_completed()
ep_robot.gimbal.moveto(pitch=-20, yaw=0, pitch_speed=80, yaw_speed=40).wait_for_completed()
ep_robot.gimbal.moveto(pitch=20, yaw=20, pitch_speed=80, yaw_speed=40).wait_for_completed()


###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
