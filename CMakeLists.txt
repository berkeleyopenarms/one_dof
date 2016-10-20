cmake_minimum_required(VERSION 2.8.3)
project(one_dof)

find_package(catkin REQUIRED COMPONENTS
  dynamixel_controllers
  roscpp
  rospy
  std_msgs
)
