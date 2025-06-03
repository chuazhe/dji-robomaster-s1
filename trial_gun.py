import time
import random
from robomaster import robot, blaster, led, chassis, gimbal, camera
import keyboard
import sys

def robot_control():
      while True:
        try:
            if keyboard.is_pressed('w'):
                print("forward！")
                ep.chassis.drive_speed(x=1, y=0, z=0, timeout=5)
                time.sleep(0.2)
                ep.chassis.drive_speed(x=0, y=0, z=0, timeout=5)
            elif keyboard.is_pressed('s'):
                print("back！")
                ep.chassis.drive_speed(x=-1, y=0, z=0, timeout=5)
                time.sleep(0.2)
                ep.chassis.drive_speed(x=0, y=0, z=0, timeout=5)
            elif keyboard.is_pressed('d'):
                print("right！")
                ep.chassis.drive_speed(x=0, y=1, z=0, timeout=5)
                time.sleep(0.2)
                ep.chassis.drive_speed(x=0, y=0, z=0, timeout=5)
            elif keyboard.is_pressed('a'):
                print("left")
                ep.chassis.drive_speed(x=0, y=-1, z=0, timeout=5)
                time.sleep(0.2)
                ep.chassis.drive_speed(x=0, y=0, z=0, timeout=5)
            elif keyboard.is_pressed('space'):
                ep_blaster.fire(fire_type=blaster.INFRARED_FIRE, times=1)
            elif keyboard.is_pressed('up'):
                ep.gimbal.move(pitch=10, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()
            elif keyboard.is_pressed('down'):
                ep.gimbal.move(pitch=-10, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()
            elif keyboard.is_pressed('right'):
                ep.gimbal.move(pitch=0, yaw=10, pitch_speed=100, yaw_speed=100).wait_for_completed()
            elif keyboard.is_pressed('left'):
                ep.gimbal.move(pitch=0, yaw=-10, pitch_speed=100, yaw_speed=100).wait_for_completed()
            elif keyboard.is_pressed('1'):
                print("Play sound!")
                ep.play_sound(robot.SOUND_ID_SCANNING).wait_for_completed()
                ep.play_sound(robot.SOUND_ID_RECOGNIZED).wait_for_completed()
            elif keyboard.is_pressed('2'):
                print("Light up!!")
                R_color = random.randint(0, 255)
                G_color = random.randint(0, 255)
                B_color = random.randint(0, 255)
                ep.led.set_led(comp="all", r=R_color, g=G_color, b=B_color, effect="on")
                time.sleep(0.5)
            elif keyboard.is_pressed('3'):
                print("Dance!!")
                dance()
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                ep.play_sound(robot.SOUND_ID_COUNT_DOWN).wait_for_completed()
                ep.close()
                sys.exit("Bye")
        except Exception as e:
            print(e)


def dance():
    bright = 1
    for i in range(0, 8):
        ep_led.set_led(comp=led.COMP_ALL, r=bright << i, g=bright << i, b=bright << i, effect=led.EFFECT_ON)
        time.sleep(1)
        print("brightness: {0}".format(bright << i))

    ep_chassis.drive_speed(x=0, y=0, z=30, timeout=5)
    it = 0
    for i in range(0, 8):
        led1 = it % 8
        led2 = (it + 1) % 8
        led3 = (it + 2) % 8
        it += 1
        ep_led.set_gimbal_led(comp="top_all", r=255, g=25, b=25,
                              led_list=[led1, led2, led3], effect=led.EFFECT_ON)
        print("Gimbal Led: {0} {1} {2} is on!".format(led1, led2, led3))
        time.sleep(0.5)
        ep_blaster.fire(fire_type=blaster.INFRARED_FIRE, times=1)
    time.sleep(1)


if __name__ == '__main__':
    ep = robot.Robot()
    ep.initialize(conn_type="ap")

    version = ep.get_version()
    print(f"Robot version: {version}")
    ep_chassis = ep.chassis
    ep_led = ep.led
    ep_blaster = ep.blaster
    ep_gimbal = ep.gimbal

    ep.set_robot_mode(mode=robot.CHASSIS_LEAD)
    robot_control()
