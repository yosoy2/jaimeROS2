# kobuki_sim

Clonar el repositorio en un workspace, en una terminal escribimos lo siguiente.

*cd ~/$workspace$/src*

*git clone $url$*

*cd ~/$workspace$*

Compilamos.

*colcon build --packages-select kobuki_sim*

## Instalar pkgs:
En una terminia correr los siguientes comandos.

*sudo apt install ros-foxy-xacro*

*sudo apt install ros-foxy-joint-state-publisher*

*sudo apt install ros-foxy-joint-state-publisher-gui*

*sudo apt update*

## Instalar gazebo con sus pkgs:
*sudo apt install gazebo11*

*sudo apt install ros-foxy-gazebo-ros-pkgs*

*sudo apt update*

## Launch:
En la primera terminal lanzar el siguiente comando.

*ros2 launch kobuki_sim rsp.launch.py use_sim_time:=true*

En una terminal nueva para cada uno lanzar los siguientes comandos.

### Lanzar Gazebo:
Abrimos gazebo.

*gazebo: ros2 launch gazebo_ros gazebo.launch.py*

Invocamos al robot.

*ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bot_name*

### Lanzar Rviz2:
Abrimos Rviz.

*rviz2*

Configuramos, Reference Frame = base_link, add RobotModel con alpha = 0.8 y Description Topic = /robot_description, add TF enable.

Corremos las transformadas generadas por joint state publisher gui.

*ros2 run joint_state_publisher_gui joint_state_publisher_gui*
