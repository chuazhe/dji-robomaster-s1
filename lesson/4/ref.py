x = 100
str1 = "Hello"
pi_2 = 3.14
Coding = "python"#导入编程操控机器人需要的模块
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
R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="bottom_front",r=R_color,g=G_color,b=B_color,effect="on")

R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="bottom_left",r=R_color,g=G_color,b=B_color,effect="on")

R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="bottom_back",r=R_color,g=G_color,b=B_color,effect="on")

R_color = random.randint(0, 255)
G_color = random.randint(0, 255)
B_color = random.randint(0, 255)
print(R_color)
print(G_color)
print(B_color)
ep_robot.led.set_led(comp="bottom_right",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(5)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="off")

###结束机器人程序###
ep_robot.close()result = (1+100)*100/2
print(result)a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)num_old = 356
n_1 = num_old % 10
n_10 = (num_old // 10) % 10
n_100 = num_old // 100
num_new = (n_1 * 100) + (n_10 * 10) + n_100
print(num_old)
print(num_new)head = 14
leg = 38

rabbit = (leg - (head * 2))/2
chicken = head - rabbit

print(chicken)
print(rabbit)
R = 256
G = 256
B = 256
num_color = R*G*B
n = 2**24
print(num_color)
print(n)#导入编程操控机器人需要的模块
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

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块
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
R_color = 20
ele_1 = 4      #密码规则因素1
ele_2 = 15     #密码规则因素2
G_color = R_color * ele_1 - ele_2
B_color = G_color * ele_1 - ele_2
print(R_color)
print(G_color)
print(B_color)

ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="on")
time.sleep(5)
ep_robot.led.set_led(comp="all",r=R_color,g=G_color,b=B_color,effect="off")

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
R_color = random.randint(0, 255)
print(R_color)
ep_robot.led.set_led(comp="all",r=R_color,g=0,b=0,effect="on")
time.sleep(5)
ep_robot.led.set_led(comp="all",r=R_color,g=0,b=0,effect="off")

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