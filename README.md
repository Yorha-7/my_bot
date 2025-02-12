you will need Nav2 package after continuing for SLAM:
command to downlode: sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup (one line code)
then you can use a launch file that will launch all the required node to use nav2 by:
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true

use goal pose to let nav2 nodes know where you want you bot, it will control bot on topic /cmd_vel
