#!/bin/bash
set -e

# If this container has a ROS2 workspace, run as ROS node
if [ -d "/ros2_ws/src" ]; then
  echo "Detected ROS2 workspace — building and launching node..."

  source /opt/ros/humble/setup.bash
  cd /ros2_ws
  colcon build

  source /ros2_ws/install/setup.bash
  ros2 run demo_package talker
else
  echo "No ROS2 workspace found — running as generic container..."
  source /opt/ros/humble/setup.bash
  exec "$@"
fi
