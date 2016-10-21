A lot of this stuff can seem a little intimidating to do if you don't have much experience with ROS/Linux/terminals (the upcoming wall of text probably doesn't help), but this is good stuff to get experience with and the best way to do so (in my opinion) is just to dive straight in. ROS has really good [tutorials](http://wiki.ros.org/ROS/Tutorials) too, if you're interested in learning it in a more procedural way.

Shoot me a message on Facebook or give me a call if you have any questions! - brent

# workspace setup
I've only run the dynamixels on my laptop so far, so none of this has been set up on the desktop yet. If you want to run the 1-dof and I haven't gotten around to setting stuff up, doing so should be a pretty straightforward process:
1. Open a terminal
2. Install the dynamixel stack & rqt_ez_publisher, which we'll use for publishing commands to the dynamixel
 - `sudo apt-get install -y ros-indigo-dynamixel-motor ros-indigo-rqt-ez-publisher`
 - `rm ~/.config/ros.org/rqt_gui.ini`
3.  create a catkin workspace
- ``mkdir -p ~/onedof_workspace/src``
- ``cd ~/onedof_workspace/src``
- ``catkin_init_workspace``
4. Clone this package into the workspace's source directory
 - ``cd ~/onedof_workspace/src``
 - ``git clone https://github.com/brentyi/one_dof.git``
5. Build our workspace
 - ``cd ~/onedof_workspace``
 - ``catkin_make``

# running
0. Plug the USB2Dynamixel into the computer, power adapter into an outlet, and the dynamixel itself to the 3-pin TTL port on the side of the USB2Dynamixel
 - it might be good to try with a motor that's not on the 1-dof first, or take the belt off the 1-dof just in case something bad happens
1. Source our workspace's setup.bash. This effectively runs a setup script that sets up a bunch of environmental variables and lets us run all the stuff in our workspace.
 - ``source ~/onedof_workspace/devel/setup.bash``
2. Launch all of our dynamixel nodes
 - ``roslanch one_dof run.launch``
3. Run rqt_ez_publisher in a new terminal. This provides a GUI for publishing to our motor control ROS topic:
 - ``rosrun rqt_ez_publisher rqt_ez_publisher``
 - protip: you can make new tabs, split the window, etc in Terminator by right clicking
4. Use the rqt_ez_publisher GUI to add `/motor_controller/command` 
 - this should be an absolute motor position in radians, so keep that in mind when setting the min/max values
 - [documentation](http://wiki.ros.org/rqt_ez_publisher)
5. Drag the slider around to send new setpoints to the motor
 - it should move!

# monitoring, recording data, etc
- to print all of the motor state information that the dynamixel is spitting out, you can run `rostopic echo /motor_controller/state` in a new terminal
- you can use `rqt_plot` this data, too!
 - `rosrun rqt_plot rqt_plot`
  - use the GUI to add the topic/data you want
  - for the load, for example, just add `/motor_controller/state/load`
 - you can adjust the time scale by clicking the green checkbox and modifying the min/max X values
 - [documentation](http://wiki.ros.org/rqt_plot)
- (probably not needed) if there's some particularly interesting behavior you want to document and a video or screenshot of the plot isn't good enough for whatever reason, you can record a "bagfile" that will effectively record all the data that's being published through ROS (motor command, state, etc) and stick it in a file that can be played back. this is super useful for debugging!
  - to start recording: ``rosbag record -a -O interestingthing.bag``
  - do the interesting thing
  - CTRL+C to stop

# potential issues
- these instructions are all off the top of my head and there's a good chance there are issues/typos, so feel free to call me out if I wrote anything that's stupid or just doesn't work
- if you see a "no motors found" error, the motor ID or baud rate might be set wrong
  - download Robotis's RoboPlus software, open the Dynamixel Wizard within it, and set the ID to 1 and baud rate to 57142
- I wrote this assuming that ROS's setup.bash is sourced by default, if none of the ROS commands work (ie catkin_init_workspace, rosrun, roslaunch, etc...) you might need to do this manually
  - ``source /opt/ros/indigo/setup.bash``
