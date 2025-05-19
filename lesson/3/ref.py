#Slide 5
import time
print("绿灯亮15秒。")
time.sleep(15)
print("黄灯亮10秒。")
time.sleep(10)
print("红灯亮15秒。")
time.sleep(15)

#Slide 6
print("出发")
print("前进1000米")
print("向右转")
print("前进200米")
print("向左转")
print("前进500米")
print("到达超市")

#Slide 9
print(123)
print(3.1415)
print(999+55)
print(999.0+55.0)
print(999+55.0)

#Slide 21
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="on")
time.sleep(3)
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="off")

ep_robot.close()

#Slide 22
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

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

ep_robot.close()

#Slide 23
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

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

ep_robot.close()

#Slide 24_1
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

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

ep_robot.close()

#Slide 24_2
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="breath")

ep_robot.close()

#Slide 24_3
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_robot.led.set_led(comp="top_all",r=255,g=0,b=0,effect="scrolling")

ep_robot.close()

#Slide 26
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=0,g=255,b=0,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=0,g=0,b=255,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=0,g=0,b=255,effect="off")

ep_robot.close()
