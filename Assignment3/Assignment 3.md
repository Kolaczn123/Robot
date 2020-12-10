---

---

# Assignment 3: ROS Publisher and Subscriber

##### Task 01: Download Program the Romi32U4

This step was completed by accessing the github repo: https://github.com/venki666/RomiPi/tree/master/Arduino/Romi-RPi-I2CSlave

This code was used to program the Romi32U4 as an I2C Slave.

##### Task 02: Setup the ROS environment

ROS melodic was installed on the NVIDIA Jetson Xavier NX and the github repository was cloned into the source folder to include the romipi_teleop package. ROSberryPi ROS melodic was also installed for the RPi 4 by completing this tutoria: http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi. A new catkin workspace was then created where the romipi_astar package was downloaded from the repository. Several dependencies had to be manually fulfilled in order to get the romipi_astar catkin_make to successfully build the package. Additional packages that were included were actionlib, angles, common_msgs, geometry, and geometry2. Additionally, some of these packages included packages that required more dependencies not necessary for this project and they were removed. After completing this process, the romipi_astar.launch successfully creates a node. The video demonstration shows that both of these packages successfully compile and execute. It is also possible to view the topics created by these nodes over the network. One thing to note is that the romipi_astar package must be installed on a RPi with I2C interface enabled.



***ROS RomiPi Publisher & Subscriber Demo*** https://youtu.be/pHBUICjTluo



