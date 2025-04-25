import time
from robomaster import robot, blaster, led, chassis, gimbal

red = 255
green = 0
blue = 0

x_val = 0.2
y_val = 0.3
z_val = 30

def robot_control(run):
    ep_led.set_led(comp=led.COMP_ALL, r=red, g=green, b=blue, effect=led.EFFECT_ON)
    if run == ord('w'):
        print("forward！")
        ep.chassis.drive_speed(0.5, 0, 0)
    elif run == ord('s'):
        print("back！")
        ep.chassis.drive_speed(-0.5, 0, 0)
    elif run == ord('a'):
        print("left")
        ep.chassis.drive_speed(0, -0.5, 0)
    elif run == ord('d'):
        print("right！")
        ep.chassis.drive_speed(0, 0.5, 0)
    elif run == ord('1'):
        print("Play sound!")
        ep_robot.play_sound(robot.SOUND_ID_SCANNING).wait_for_completed()
        ep_robot.play_sound(robot.SOUND_ID_RECOGNIZED).wait_for_completed()
    elif run == ord('2'):
        print("Move gimbal!")
        ep_gimbal.move(pitch=0, yaw=-100).wait_for_completed()
        ep_gimbal.recenter().wait_for_completed()
        ep_gimbal.move(pitch=0, yaw=100).wait_for_completed()
        ep_gimbal.recenter(pitch_speed=100, yaw_speed=100).wait_for_completed()
        ep_gimbal.recenter().wait_for_completed()
    elif run == ord('3'):
        print("Go!")
        ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
        ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
        ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=0.7).wait_for_completed()
        ep_chassis.move(x=0, y=y_val, z=0, xy_speed=0.7).wait_for_completed()
    elif run == ord('4'):
        shoot()
        # grip()
    elif run == ord('5'):
        dance()
    elif run == ord('6'):
        ep_camera.start_video_stream(display=True, resolution=camera.STREAM_360P)
        time.sleep(10)
        ep_camera.stop_video_stream()
    elif run == ord('0'):
        ep_robot.play_sound(robot.SOUND_ID_COUNT_DOWN).wait_for_completed()
        ep_robot.close()
        sys.exit("Bye") 

def shoot():
    print("Shoot!")
    ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
    time.sleep(1)
    ep_blaster.set_led(brightness=32, effect=blaster.LED_ON)
    time.sleep(1)
    ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
    time.sleep(1)
    ep_blaster.set_led(brightness=64, effect=blaster.LED_ON)
    time.sleep(1)
    ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
    time.sleep(1)
    ep_blaster.set_led(brightness=128, effect=blaster.LED_ON)
    time.sleep(1)
    ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
    time.sleep(1)
    ep_blaster.set_led(brightness=255, effect=blaster.LED_ON)
    time.sleep(1)
    ep_gimbal.recenter().wait_for_completed()

def grip():
    print("Grip!")
    ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
    time.sleep(1)
    ep_gripper.open(power=50)
    time.sleep(1)
    ep_gripper.pause()
    ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
    time.sleep(1)
    ep_arm.move(x=20, y=0).wait_for_completed()
    ep_arm.move(x=0, y=20).wait_for_completed()
    time.sleep(1)
    ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
    time.sleep(1)
    ep_arm.move(x=-20, y=0).wait_for_completed()
    ep_arm.move(x=0, y=-20).wait_for_completed()
    time.sleep(1)
    ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
    time.sleep(1)
    ep_gripper.close(power=50)
    time.sleep(1)
    ep_gripper.pause()
    ep_gimbal.recenter().wait_for_completed()

def dance():
    print("Dance!")
    ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
    time.sleep(1)
    chassis_action = ep_chassis.drive_speed(x=0, y=0, z=-z_val, timeout=5)
    
    bright = 1
    for i in range(0, 8):
        ep_led.set_led(comp=led.COMP_ALL, r=bright << i, g=bright << i, b=bright << i, effect=led.EFFECT_ON)
        print("brightness: {0}".format(bright << i))
        time.sleep(0.5)
        ep_blaster.fire(fire_type=blaster.INFRARED_FIRE, times=1)
    chassis_action.wait_for_completed()

    ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
    time.sleep(1)
    chassis_action = ep_chassis.drive_speed(x=0, y=0, z=z_val, timeout=5)
    it = 0
    for i in range(0, 8):
        led1 = it % 8
        led2 = (it + 1) % 8
        led3 = (it + 2) % 8
        it += 1
        ep_led.set_gimbal_led(comp=led.COMP_TOP_ALL, r=255, g=25, b=25,
                            led_list=[led1, led2, led3], effect=led.EFFECT_ON)
        print("Gimbal Led: {0} {1} {2} is on!".format(led1, led2, led3))
        time.sleep(0.5)
        ep_blaster.fire(fire_type=blaster.INFRARED_FIRE, times=1)
    chassis_action.wait_for_completed()

def sub_data_handler(sub_info):
    print("mouse_press:{0} mouse_x:{1} mouse_y:{2} key1:{3}"
          .format(sub_info[0], sub_info[1], sub_info[2], sub_info[-1]))
    robot_control(sub_info[-1])

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    version = ep_robot.get_version()
    print(f"Robot version: {version}")
    ep_chassis = ep_robot.chassis
    ep_led = ep_robot.led
    ep_blaster = ep_robot.blaster
    ep_gimbal = ep_robot.gimbal

    ep_robot.set_robot_mode(mode=robot.CHASSIS_LEAD)
    ep_robot.sub_game_msg(callback=sub_data_handler)
