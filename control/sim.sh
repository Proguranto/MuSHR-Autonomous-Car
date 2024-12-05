#! /bin/bash 
source /opt/ros/noetic/setup.bash 
source /home/capstone/dependencies_ws/devel/setup.bash 
source /home/capstone/mushr_ws/devel/setup.bash
echo "launching the sim ros commands..."
roslaunch cse478 teleop.launch teleop:=false &
sleep 3
roslaunch control controller.launch type:=pp &
sleep 3
rosrun rviz rviz -d $(rospack find control)/config/control.rviz &
wait