# Slide 10
school = input("输入你的学校：")
grade = input("输入你的班级：")
name = input("输入你的姓名：")
print(school)
print(grade)
print(name)#导入编程操控机器人需要的模块

# Slide 11
print("""
                       ▶ Python真好玩！
                       |
                __\--__|_
II=======00000[/ ★007___|
          _____\______|/-----.
        /___    roborobo   ___|
         \◎◎◎◎◎◎◎◎◎◎/
""")


# Slide 12
a = input("输入一个字符串：")
print(len(a))

# Slide 13_1
a = input("输入一个数：")
print(type(a))
b = input("输入第二个数：")
print(type(b))
result = a+b
print(result)
print(type(result))

# Slide 13_2
a = float(input("输入第一个加数："))
b = float(input("输入第二个加数："))
result = a + b
print(str(a)+"+"+str(b)+"="+str(result))

# Slide 14_1
a = input("输入一个字符串：")
print(a+"的长度为：", len(a))

# May not be used
print("%s的长度为：%d"%(a,len(a)))
print("{0}的长度为：{1}".format(a,len(a)))

# Slide 14_2
city = input("输入城市：")
temp = float(input("输入当天气温："))
print("%s今天气温为：%.1f℃\n欢迎来到%s！"%(city,temp,city))

# Slide 15
import time
from robomaster import robot
from robomaster import led
from robomaster import blaster

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
r_color = int(input("输入前装甲灯R值(0~255)："))
g_color = int(input("输入前装甲灯G值(0~255)："))
b_color = int(input("输入前装甲灯B值(0~255)："))
ep_robot.led.set_led(comp=led.COMP_BOTTOM_FRONT, r=r_color, g=g_color, b=b_color, effect=led.EFFECT_ON)
print("机器人前装甲灯颜色为：R=%d, G=%d, B=%d"%(r_color,g_color,b_color))

r_color = int(input("输入左装甲灯R值(0~255)："))
g_color = int(input("输入左装甲灯G值(0~255)："))
b_color = int(input("输入左装甲灯B值(0~255)："))
ep_robot.led.set_led(comp=led.COMP_BOTTOM_LEFT, r=r_color, g=g_color, b=b_color, effect=led.EFFECT_ON)
print("机器人左装甲灯颜色为：R=%d, G=%d, B=%d"%(r_color,g_color,b_color))

r_color = int(input("输入后装甲灯R值(0~255)："))
g_color = int(input("输入后装甲灯G值(0~255)："))
b_color = int(input("输入后装甲灯B值(0~255)："))
ep_robot.led.set_led(comp=led.COMP_BOTTOM_BACK, r=r_color, g=g_color, b=b_color, effect=led.EFFECT_ON)
print("机器人后装甲灯颜色为：R=%d, G=%d, B=%d"%(r_color,g_color,b_color))

r_color = int(input("输入右装甲灯R值(0~255)："))
g_color = int(input("输入右装甲灯G值(0~255)："))
b_color = int(input("输入右装甲灯B值(0~255)："))
ep_robot.led.set_led(comp=led.COMP_BOTTOM_RIGHT, r=r_color, g=g_color, b=b_color, effect=led.EFFECT_ON)
print("机器人右装甲灯颜色为：R=%d, G=%d, B=%d"%(r_color,g_color,b_color))
time.sleep(5)

###结束机器人程序###
ep_robot.close()#导入编程操控机器人需要的模块

# Slide 16
from robomaster import robot
from robomaster import led
import time

###机器人初始化###
#在程序内实例化Robot对象，相当于在程序内部有一个EP机器人
#程序与机器人联网，“ap”表示直连模式连接；“sta”表示路由器模式连接；rndis表示使用USB连接
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

###你要写的程序###
"""音效名称
robot.SOUND_ID_ATTACK          被打中音效
robot.SOUND_ID_SHOOT           射击音效
robot.SOUND_ID_SCANNING        扫描音效
robot.SOUND_ID_RECOGNIZED      识别成功
robot.SOUND_ID_GIMBAL_MOVE     云台移动音效
robot.SOUND_ID_COUNT_DOWN      计数音效
"""
print("SOUND_ID_ATTACK")
ep_robot.play_sound(robot.SOUND_ID_ATTACK).wait_for_completed()
print("SOUND_ID_SHOOT")
ep_robot.play_sound(robot.SOUND_ID_SHOOT).wait_for_completed()
print("SOUND_ID_SCANNING")
ep_robot.play_sound(robot.SOUND_ID_SCANNING).wait_for_completed()
print("SOUND_ID_RECOGNIZED")
ep_robot.play_sound(robot.SOUND_ID_RECOGNIZED).wait_for_completed()
print("SOUND_ID_GIMBAL_MOVE")
ep_robot.play_sound(robot.SOUND_ID_GIMBAL_MOVE).wait_for_completed()
print("SOUND_ID_COUNT_DOWN")
ep_robot.play_sound(robot.SOUND_ID_COUNT_DOWN).wait_for_completed()

###结束机器人程序###
ep_robot.close()# This is a sample Python script.

# Slide 18
a = int(input("输入第一个数："))
b = int(input("输入第二个数："))
print("%d + %d = %d"%(a,b,a+b))
print("%d - %d = %d"%(a,b,a-b))
print("%d * %d = %d"%(a,b,a*b))
print("%d / %d = %f"%(a,b,a/b))
print("%d 余 %d = %d"%(a,b,a%b))
print("%d // %d = %d"%(a,b,a//b))
print("%d的%d次方 = %d"%(a,b,a**b))
