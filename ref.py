# import robomaster
# from robomaster import robot
# from robomaster import chassis
# from robomaster import led
# import time
# import random
#
# # Initialize the RoboMaster EP robot
# ep_robot = robot.Robot()
# ep_robot.initialize(conn_type="ap")
#
#
# def move_forward(distance, speed=2):
#     ep_robot.chassis.move(x=distance, y=0, z=0, xy_speed=speed).wait_for_completed()
#
#
# def turn(angle, speed=90):
#     ep_robot.chassis.move(x=0, y=0, z=angle, z_speed=speed).wait_for_completed()
#
#
#
# def get_user_input():
#     print("****************************************")
#     return input("Enter direction (WASDQER): ").upper()
#
#
#
# angle = 0
# print("****************************************")
# print("Enter 'w' to move forward")
# print("Enter 's' to move backwards")
# print("Enter 'a' to turn 90 degrees left")
# print("Enter 'd' to turn right")
# print("Enter 'q' to turn 45 degrees left")
# print("Enter 'e' to turn 37 degrees right")
# print("Enter 'r' to reset the robot's direction")
# print("****************************************")
#
# try:
#     while True:
#         direction = get_user_input()
#         if direction == "W":  # Move forward
#             move_forward(0.5)
#         elif direction == "S":  # Move backward
#             move_forward(-0.5)
#         elif direction == "A":  # Turn left
#             turn(90)
#             angle  = angle + 90
#         elif direction == "D":  # Turn right
#             turn(-90)
#             angle = angle - 90
#         elif direction == "E":  # 37 degree turn
#             turn(-37)
#             angle = angle - 37
#         elif direction == "Q":  # 45 degree turn
#             turn(45)
#             angle = angle + 45
#         elif direction == "R":  # Reset direction facing
#             turn(-angle)
#             angle = 0
#         else:
#             print("Incorrect key entered! Please try again.")
#
# except KeyboardInterrupt:
#     # Cleanup and close the robot connection on interrupt
#     print("Program interrupted. Closing the robot connection.")
#     ep_robot.close()

# print("                      |> Python is so fun!")
# print("                      |                  ")
# print("               __\--__|_                 ")
# print("II=======00000{/ *007___|                ")
# print("           ____\_____|/-----.            ")
# print("          /___  roborobo  ___|           ")
# print("          \OOOOOOOOOOOOOOOOO)/           ")

# r_front = input("Input the R value of the front armour light (0-255): ")
# g_front = input("Input the G value of the front armour light (0-255): ")
# b_front = input("Input the B value of the front armour light (0-255): ")
# ep_robot.led.set_led(comp='bottom_front', r=int(r_front), g=int(g_front), b=int(b_front), effect='on', freq=1)
# print("The colour of the robot's front armour light is: R = " + r_front + ", G = " + g_front + ", B = " + b_front)
# r_left = input("Input the R value of the left armour light (0-255): ")
# g_left = input("Input the G value of the left armour light (0-255): ")
# b_left = input("Input the B value of the left armour light (0-255): ")
# ep_robot.led.set_led(comp='bottom_left', r=int(r_left), g=int(g_left), b=int(b_left), effect='on', freq=1)
# print("The colour of the robot's left armour light is: R = " + r_left + ", G = " + g_left + ", B = " + b_left)
# r_rear = input("Input the R value of the rear armour light (0-255): ")
# g_rear = input("Input the G value of the rear armour light (0-255): ")
# b_rear = input("Input the B value of the rear armour light (0-255): ")
# ep_robot.led.set_led(comp='bottom_back', r=int(r_rear), g=int(g_rear), b=int(b_rear), effect='on', freq=1)
# print("The colour of the robot's rear armour light is: R = " + r_rear + ", G = " + g_rear + ", B = " + b_rear)
# r_right = input("Input the R value of the right armour light (0-255): ")
# g_right = input("Input the G value of the right armour light (0-255): ")
# b_right = input("Input the B value of the right armour light (0-255): ")
# ep_robot.led.set_led(comp='bottom_right', r=int(r_right), g=int(g_right), b=int(b_right), effect='on', freq=1)
# print("The colour of the robot's right armour light is: R = " + r_right + ", G = " + g_right + ", B = " + b_right)
#
# time.sleep(5)
#
# ep_robot.close()

# a = input("Enter your first integer: ")
# b = input("Enter your second integer: ")
#
# c = int(a)+int(b)
# d = int(a)-int(b)
# e = int(a)*int(b)
# f = int(a)/int(b)
# g = int(a)%int(b)
# h = int(a)//int(b)
# i = int(a)**int(b)
#
# print(a + " + " + b + " = " + str(c))
# print(a + " - " + b + " = " + str(d))
# print(a + " * " + b + " = " + str(e))
# print(a + " / " + b + " = " + str(f))
# print(a + " % " + b + " = " + str(g))
# print(a + " // " + b + " = " + str(h))
# print(a + " ** " + b + " = " + str(i))

import robomaster
from robomaster import robot
from robomaster import blaster
import time

# Initialize the RoboMaster EP robot
ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")

# ep_robot.gimbal.drive_speed(pitch_speed=0,yaw_speed=100.0)
# time.sleep(1)
# ep_robot.gimbal.drive_speed(pitch_speed=0,yaw_speed=-100.0)
# time.sleep(1)
# ep_robot.gimbal.drive_speed(pitch_speed=15,yaw_speed=0)
# time.sleep(1)
# ep_robot.gimbal.drive_speed(pitch_speed=-15,yaw_speed=0)
# time.sleep(1)

ep_robot.gimbal.moveto(pitch=0,yaw=50,pitch_speed=50,yaw_speed=50).wait_for_completed()

ep_robot.close()

# def move_in_circle(radius=0.5, rpm=50, duration=10):
#     # Calculate wheel speeds in meters per second
#     wheel_diameter = 0.1  # Assume wheel diameter is 0.1 meters (10 cm)
#     wheel_circumference = 3.14159 * wheel_diameter
#
#     # Convert RPM to meters per second
#     speed_mps = (rpm * wheel_circumference) / 60  # Speed of each wheel in m/s
#
#     # Calculate the angular velocity for the circular motion (in radians per second)
#     angular_velocity = speed_mps / radius
#
#     # Calculate linear velocities for inner and outer wheels
#     inner_wheel_speed_mps = angular_velocity * (radius - wheel_diameter / 2)
#     outer_wheel_speed_mps = angular_velocity * (radius + wheel_diameter / 2)
#
#     # Convert linear speeds to RPM for the `drive_wheels` function
#     inner_wheel_rpm = (inner_wheel_speed_mps * 60) / wheel_circumference
#     outer_wheel_rpm = (outer_wheel_speed_mps * 60) / wheel_circumference
#
#     # Speeds for each wheel (assuming clockwise movement)
#     w1_rpm = outer_wheel_rpm  # Front-left
#     w2_rpm = inner_wheel_rpm  # Front-right
#     w3_rpm = outer_wheel_rpm  # Rear-left
#     w4_rpm = inner_wheel_rpm  # Rear-right
#
#     print(f"Calculated speeds (RPM): w1={w1_rpm:.2f}, w2={w2_rpm:.2f}, w3={w3_rpm:.2f}, w4={w4_rpm:.2f}")
#
#     start_time = time.time()
#     while (time.time() - start_time) < duration:
#         ep_robot.chassis.drive_wheels(w1=w1_rpm, w2=w2_rpm, w3=w3_rpm, w4=w4_rpm)
#         time.sleep(0.1)  # Small delay to create smooth motion
#
# try:
#     move_in_circle(radius=0.5, rpm=50, duration=10)
#
# except KeyboardInterrupt:
#     # Cleanup and close the robot connection on interrupt
#     print("Program interrupted. Closing the robot connection.")
#     ep_robot.close()
#
# # Stop the robot and close the connection
# ep_robot.chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)
# ep_robot.close()






