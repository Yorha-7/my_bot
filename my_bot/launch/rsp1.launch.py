import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Declare the use_sim_time launch argument
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation time if true'
    )

    # Get the path to the URDF Xacro file
    pkg_path = os.path.join(get_package_share_directory('my_bot'))
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro')
    
    # Process the Xacro file into a URDF string
    robot_description_config = xacro.process_file(xacro_file)

    # Create the robot_state_publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_config.toxml(),
            'use_sim_time': LaunchConfiguration('use_sim_time')
        }]
    )

    # Launch description
    return LaunchDescription([
        declare_use_sim_time,  # Declare the launch argument

        # Launch joint_state_publisher_gui,

        # Launch the robot_state_publisher node
        robot_state_publisher_node
    ])

