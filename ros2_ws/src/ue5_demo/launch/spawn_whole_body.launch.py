# turtlesim/launch/multisim.launch.py

import os
from launch import LaunchDescription
import launch_ros.actions
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    param_file_path = os.path.join(
        get_package_share_directory('ue5_demo'),
        'config',
        'params.yaml'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'param_file',
            default_value=param_file_path,
            description='Path to the parameter file'),
        launch_ros.actions.Node(
            namespace= "ur5", package='ue5_demo', output='screen', parameters=LaunchConfiguration('param_file')),
        launch_ros.actions.Node(
            namespace= "turtlesim2", package='turtlesim', executable='turtlesim_node', output='screen'),
    ])