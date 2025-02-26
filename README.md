# tcebot_sim

## Overview

`tcebot_sim` is a ROS 2 package designed for simulating the `tcebot` robot in a Gazebo environment. It provides predefined worlds, launch files, and configurations to facilitate robot simulation.

## Installation

To install this package in your ROS 2 workspace:

```bash
cd ~/ros2_ws/src
git clone https://github.com/dhanushshettigar/tcebot_sim.git
cd ~/ros2_ws
colcon build --packages-select tcebot_sim
source install/setup.bash
```

## Usage

Launch Simulation

```bash
ros2 launch tcebot_sim simulation.launch.py
```
Spawn tcebot in Gazebo

```bash
ros2 launch tcebot_sim spawn_tcebot.launch.py
```
