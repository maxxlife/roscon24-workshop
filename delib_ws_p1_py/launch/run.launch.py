from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

problem_pkg = get_package_share_directory("delib_ws_p1")


def generate_launch_description():
    # Problem node
    problem_node = Node(package="delib_ws_p1", executable="run", name="run")
    # Solution node
    solution_node = Node(package="delib_ws_p1_py", executable="run", name="run")

    return LaunchDescription([problem_node, solution_node])
