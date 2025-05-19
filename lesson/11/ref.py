# Slide 
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
while True:
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=0, effect=led.EFFECT_ON)
    time.sleep(1)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=255, g=255, b=255, effect=led.EFFECT_ON)
    time.sleep(1)
###结束机器人程序###
ep_robot.close()




# Slide 
# 导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
while True:
    ep_robot.led.set_led(comp=led.COMP_ALL, r=255, g=0, b=0, effect=led.EFFECT_ON)
    time.sleep(1)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=255, b=0, effect=led.EFFECT_ON)
    time.sleep(1)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_ON)
    time.sleep(1)
###结束机器人程序###
ep_robot.close()





# Slide 
# 导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
while True:
    ep_robot.led.set_led(comp=led.COMP_ALL, r=255, g=0, b=0, effect=led.EFFECT_ON)
    ep_robot.chassis.move(x=0, y=0, z=-90, z_speed=45).wait_for_completed()
###结束机器人程序###
ep_robot.close()




# Slide 
# 导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
while True:
    a = input("请输入方向（w/a/s/d）:")
    if a == 'w':
        ep_robot.chassis.move(x=0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()

    elif a == 's':
        ep_robot.chassis.move(x=-0.5, y=0, z=0, xy_speed=0.7).wait_for_completed()

    elif a == 'a':
        ep_robot.chassis.move(x=0, y=-0.6, z=0, xy_speed=0.7).wait_for_completed()

    elif a == 'd':
        ep_robot.chassis.move(x=0, y=0.6, z=0, xy_speed=0.7).wait_for_completed()
    else:
        print("输入有误！！！请重新输入。")
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


def hit_callback(sub_info, ep_robot):
    armor_id, hit_type = sub_info
    print("hit event: hit_comp:{0}, hit_type:{1}".format(armor_id, hit_type))
    ###你要写的程序###
    ep_robot.blaster.fire(times=1)


ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")
ep_robot.armor.set_hit_sensitivity(comp="all", sensitivity=5)
ep_robot.armor.sub_hit_event(hit_callback, ep_robot)
time.sleep(5)
ep_robot.armor.unsub_hit_event()
###结束机器人程序###
ep_robot.close()




# Slide 
# 导入编程操控机器人需要的模块
import robomaster
from robomaster import robot
from robomaster import blaster
import time

###机器人初始化###
# 在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
# 程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

def hit_callback(sub_info, ep_robot):
    armor_id, hit_type = sub_info
    print("hit event: hit_comp:{0}, hit_type:{1}".format(armor_id, hit_type))
    ###你要写的程序###
    ep_robot.gimbal.moveto(pitch=0, yaw=0).wait_for_completed()
    ep_robot.blaster.fire(times=3)
    
###结束###
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")
ep_robot.armor.set_hit_sensitivity(comp="all", sensitivity=5)
ep_robot.armor.sub_hit_event(hit_callback, ep_robot)
time.sleep(5)
ep_robot.armor.unsub_hit_event()
###结束机器人程序###
ep_robot.close()
# 导入编程操控机器人需要的模块



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

def hit_callback(sub_info, ep_robot):
    armor_id, hit_type = sub_info
    print("hit event: hit_comp:{0}, hit_type:{1}".format(armor_id, hit_type))
    ###你要写的程序###
    ep_robot.led.set_led(comp=led.COMP_ALL, r=255, g=0, b=0, effect=led.EFFECT_ON)
    ep_robot.play_sound(robot.SOUND_ID_ATTACK).wait_for_completed()
    time.sleep(1)
    ep_robot.led.set_led(comp=led.COMP_ALL, r=0, g=0, b=255, effect=led.EFFECT_ON)


###结束###
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")
ep_robot.armor.set_hit_sensitivity(comp="all", sensitivity=5)
ep_robot.armor.sub_hit_event(hit_callback, ep_robot)
time.sleep(5)
ep_robot.armor.unsub_hit_event()
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


def hit_callback(sub_info, ep_robot):
    armor_id, hit_type = sub_info
    print("hit event: hit_comp:{0}, hit_type:{1}".format(armor_id, hit_type))
    ###你要写的程序###
###结束###


# Slide 
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")
ep_robot.armor.set_hit_sensitivity(comp="all", sensitivity=5)
ep_robot.armor.sub_hit_event(hit_callback, ep_robot)
time.sleep(5)
ep_robot.armor.unsub_hit_event()
###结束机器人程序###
ep_robot.close()

