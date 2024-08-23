# Setup for panda moveit demo

## Install moveit dependencies
*assumes ros2 humble is already installed*

```
source /opt/ros/humble/setup.bash
```

Install rosdep to install system dependencies:
```
sudo apt install python3-rosdep
```


Once you have ROS 2 installed, make sure you have the most up to date packages:
```
sudo rosdep init
rosdep update
sudo apt update
sudo apt dist-upgrade
```

Install Colcon the ROS 2 build system with mixin:
```
sudo apt install python3-colcon-common-extensions
sudo apt install python3-colcon-mixin
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update default
```

Install vcstool :
```
sudo apt install python3-vcstool
```

For tutorials you will need to have a colcon workspace setup.
```
mkdir -p ~/ws_moveit2/src
```

Move into your Colcon workspace and pull the MoveIt tutorials source:
```
cd ~/ws_moveit2/src
git clone --branch humble https://github.com/ros-planning/moveit2_tutorials
```

Next we will download the source code for the rest of MoveIt:
```
vcs import < moveit2_tutorials/moveit2_tutorials.repos
```

The following will install from Debian any package dependencies not already in your workspace. This is the step that will install MoveIt and all of its dependencies:
```
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

The next command will configure your Colcon workspace:
```
cd ~/ws_moveit2
colcon build --mixin release
```

Source the Colcon workspace:
```
source ~/ws_moveit2/install/setup.bash
```

Optional: add the previous command to your .bashrc:
```
echo 'source ~/ws_moveit2/install/setup.bash' >> ~/.bashrc
```