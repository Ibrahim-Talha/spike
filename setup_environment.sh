#!/bin/bash 

#THE PATH OF THE PROJECT!
export PROJECT_DIR="/home/lars/Desktop/project"

#ADD THIS FILE TO BE EXECUTED EVERY TIME A BASH TERMINAL IS OPENED
#IF PROJECT_DIR CHANGES YOU SHOULD REMOVE THE OUTDATED LINE FROM ~/.bashrc
environment_file="source $PROJECT_DIR/setup_environment.sh"
grep -qxF "$environment_file" ~/.bashrc || echo $environment_file >> ~/.bashrc

#MAKE PYTHON AND PIP AVAILABLE TO BASH
export PATH="~/.local/bin:$PATH"

#MAKE ROS PACKAGED AVAILABLE TO BASH
source /opt/ros/noetic/setup.bash
source $PROJECT_DIR/devel/setup.bash

#ENVIRONMENT VARIABLES NEEDED FOR UNITREE COMPONENTS
export ROS_PACKAGE_PATH=$PROJECT_DIR/src:${ROS_PACKAGE_PATH} #TODO: See if still needed
export GAZEBO_PLUGIN_PATH=$PROJECT_DIR/devel/lib:${GAZEBO_PLUGIN_PATH} #TODO: See if still needed
export LD_LIBRARY_PATH=$GAZEBO_PLUGIN_PATH:${LD_LIBRARY_PATH} #TODO: See if still needed

export UNITREE_SDK_VERSION="3_2" #TODO: Remove usage of this variable in unitree_legged_real
export UNITREE_LEGGED_SDK_PATH="$PROJECT_DIR/include/unitree_legged_sdk"
export UNITREE_PLATFORM="amd64"







