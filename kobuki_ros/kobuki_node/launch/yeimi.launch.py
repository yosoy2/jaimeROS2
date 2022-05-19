
from launch import LaunchDescription

def generate_launch_description():
    ld = LaunchDescription()
    base_launch = Node(
        package="demo_nodes_cpp",
        executable="talker",
    )
    listener_node = Node(
        package="demo_nodes_py",
        executable="listener"
    )
    ld.add_action(talker_node)
    ld.add_action(listener_node)
    return ld
