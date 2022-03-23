# ENAMOUR Informatics ROS A1 Project

To build the project execute "source make.sh". This will also execute "source setup_environment.sh".

Be aware, the execution of ROS commands should be done via sudo, since system calls like semaphores will be used.
You can change to the sudo user by using "sudo -s".

To test the project:
- Build the project 
- Execute "sudo roslaunch champ_config bringup.launch rviz:=true"
- In another terminal (CTRL + SHIFT + T) execute "sudo roslaunch champ_teleop teleop.launch".

To commit to this repo via vm, execute the setup_git.sh file:
./setup_git.sh "thi-username"
