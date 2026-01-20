import robomaster
from robomaster import robot
import time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")

ep_robot.camera.start_video_stream()
time.sleep(100)
ep_robot.camera.stop_video_stream()  # 关闭视频流

ep_robot.close()
