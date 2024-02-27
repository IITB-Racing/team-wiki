# MRPT using ros1_bridge in eufs_sim

Currently I've ros2: galactic. Need to setup ros-bridge by installing ros1, and setting-up all repos:

1. install ros1: noetic (Ubuntu 20.04): [Ubuntu install of ROS Noetic](https://wiki.ros.org/noetic/Installation/Ubuntu)
2. clone repos (ros-bridge branch): [iitbdv](https://github.com/dv-software-22-23/IITBdv), [iitb-racing-ros2](https://github.com/IIT-Bombay-Racing-Driverless/iitb-racing-ros2) (I'd to force pull since I'd some conflicting changes)
3. install mrpt using `readme.md` in IITBdv.
4. Build both workspaces
	- while building IITBdv: `catkin: command not found` -> `sudo apt-get install ros-noetic-catkin python3-catkin-tools`
	- tried launching: `roslaunch mrpt-fsds mrpt_fsds_rosbag.launch`. Working.
5. Missed cloning (use correct branch for your ros version): [ros1_bridge](https://github.com/ros2/ros1_bridge). Cloned it under src of a new wrkspc: ros1_bridge_ws, built it using `build.sh` provided by vishwam
6. Order of launching nodes:
	1. launch eufs: `ros2 launch eufs_launcher eufs_launcher.launch.py`
	2. fake_meas_eufs: `ros2 run perception fake_meas_eufs`
	3. `mrpt_eufs.launch` from IITBdv.
	4. run ros1_bridge: `ros2 run ros1_bridge dynamic_bridge`

This worked for running mrpt using ros1-bridge for EUFS. We can probably set-up new a single launch file for all ros2 nodes (ros1_bridge, fake_meas, eufs).