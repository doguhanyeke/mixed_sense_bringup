import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

def generate_launch_description():
    xrce_gps_bridge_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('px4_gps'), 'launch', 'px4_gps_xrce_attack_herding_glas.launch.py')),
        launch_arguments={
            'px4_ns': "px4_1",
            'gz_world_name': "swarm_herding_glas",
            'gz_model_name': "x500_1",
            'gz_spoofer_model_name': "spoofer",
            'gps_delay': '0.0'
        }.items(),
    )
    xrce_gps_bridge_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('px4_gps'), 'launch', 'px4_gps_xrce_attack_herding_glas.launch.py')),
        launch_arguments={
            'px4_ns': "px4_2",
            'gz_world_name': "swarm_herding_glas",
            'gz_model_name': "x500_2",
            'gz_spoofer_model_name': "spoofer",
            'gps_delay': '0.0'
        }.items(),
    )
    xrce_gps_bridge_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('px4_gps'), 'launch', 'px4_gps_xrce_attack_herding_glas.launch.py')),
        launch_arguments={
            'px4_ns': "px4_3",
            'gz_world_name': "swarm_herding_glas",
            'gz_model_name': "x500_3",
            'gz_spoofer_model_name': "spoofer",
            'gps_delay': '0.0'
        }.items(),
    )
    
    vis_1 = Node(
        package='px4_offboard',
        executable='visualizer_swarm',
        name='visualizer_swarm',
        parameters=[
            {'px4_ns': 'px4_1'},
            {'initial_position': [-8.0, -6.0]},
        ]   
    )

    vis_2 = Node(
        package='px4_offboard',
        executable='visualizer_swarm',
        name='visualizer_swarm',
        parameters=[
            {'px4_ns': 'px4_2'},
            {'initial_position': [-8.0, -8.0]},
        ]   
    )
    
    vis_3 = Node(
        package='px4_offboard',
        executable='visualizer_swarm',
        name='visualizer_swarm',
        parameters=[
            {'px4_ns': 'px4_3'},
            {'initial_position': [-8.0, -10.0]},
        ]   
    )

    foxglove_studio = ExecuteProcess(cmd=["foxglove-studio"])
    foxglove_bridge = IncludeLaunchDescription(XMLLaunchDescriptionSource(
        os.path.join(
        get_package_share_directory("mixed_sense_bringup"),
        "launch/foxglove_bridge.launch",))
    )
    return LaunchDescription([
        xrce_gps_bridge_1,
        xrce_gps_bridge_2,
        xrce_gps_bridge_3,
        vis_1,
        vis_2,
        vis_3,
        foxglove_bridge,
        foxglove_studio
    ])
