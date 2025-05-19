# Slide 5
x = 100
str1 = "Hello"
pi_2 = 3.14
Coding = "python"

# Slide 6
result = (1+100)*100/2
print(result)

# Slide 7_1
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Slide 7_2
head = 14
leg = 38
rabbit = (leg - (head * 2))/2
chicken = head - rabbit
print(chicken)
print(rabbit)

# Slide 11
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random




ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")


R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(2)

R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(2)


ep_robot.close()

# Slide 12_1
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random




ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")


R_color = random.randint(0, 255)
print(R_color)
ep_robot.led.set_led(comp="all",r=R_color,g=0,b=0,effect="on")
time.sleep(5)
ep_robot.led.set_led(comp="all",r=R_color,g=0,b=0,effect="off")


ep_robot.close()

# Slide 12_2
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time
import random




ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")


R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(2)

R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(2)

R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(2)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="off")


ep_robot.close()

# Slide 12_3
import robomaster
from robomaster import robot
from robomaster import led
from robomaster import blaster
import time




ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")


r_data = 255
g_data = 255
b_data = 0
ep_robot.led.set_led(comp="all",r=r_data,g=g_data,b=b_data,effect="on")
time.sleep(2)

r_data = 255
g_data = 0
b_data = 255
ep_robot.led.set_led(comp="all",r=r_data,g=g_data,b=b_data,effect="on")
time.sleep(2)

r_data = 0
g_data = 255
b_data = 255
ep_robot.led.set_led(comp="all",r=r_data,g=g_data,b=b_data,effect="on")
time.sleep(2)

ep_robot.led.set_led(comp="all",r=r_data,g=g_data,b=b_data,effect="off")


ep_robot.close()
