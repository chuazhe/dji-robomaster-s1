from robomaster import robot
from robomaster import led
from robomaster import blaster
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")


""""
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
"""

# Set the LED to red color for 2 seconds
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="on")
time.sleep(2)


# Set the LED off
ep_robot.led.set_led(comp="all",r=255,g=0,b=0,effect="off")


"""
robot.SOUND_ID_ATTACK          
robot.SOUND_ID_SHOOT           
robot.SOUND_ID_SCANNING        
robot.SOUND_ID_RECOGNIZED      
robot.SOUND_ID_GIMBAL_MOVE     
robot.SOUND_ID_COUNT_DOWN      
"""
print("SOUND_ID_ATTACK")
ep_robot.play_sound(robot.SOUND_ID_ATTACK).wait_for_completed()


"""
ep_robot.chassis.drive_speed(x=1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=-1,y=0,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=1,z=0,timeout=5)
time.sleep(1)
ep_robot.chassis.drive_speed(x=0,y=-1,z=0,timeout=5)
time.sleep(1)

ep_robot.chassis.move(x=1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=-1,y=0,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=1,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=-1,z=0,xy_speed=1,z_speed=0).wait_for_completed()
ep_robot.chassis.move(x=0,y=0,z=90,xy_speed=0,z_speed=30).wait_for_completed()
ep_robot.chassis.move(x=0,y=0,z=-90,xy_speed=0,z_speed=30).wait_for_completed()

ep_chassis.drive_wheels(w1=speed, w2=speed, w3=speed, w4=speed)
time.sleep(slp)

ep_chassis.drive_wheels(w1=-speed, w2=-speed, w3=-speed, w4=-speed)
time.sleep(slp)

ep_chassis.drive_wheels(w1=speed, w2=-speed, w3=speed, w4=-speed)
time.sleep(slp)

ep_chassis.drive_wheels(w1=-speed, w2=speed, w3=-speed, w4=speed)
time.sleep(slp)
"""

""""
ep_robot.gimbal.move(pitch=0, yaw=50, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.gimbal.move(pitch=10, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()
ep_robot.gimbal.move(pitch=0, yaw=-100, pitch_speed=100, yaw_speed=100).wait_for_completed()
"""

# Shoot the blaster 3 times with infrared fire
ep_robot.blaster.fire(fire_type=blaster.INFRARED_FIRE, times=3)

ep_robot.close()
