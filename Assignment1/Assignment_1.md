# Assignment 1

Using the code supplied in [here](https://github.com/venki666/CpE476_demos/tree/master/Arduino/Romi-NoRpi-Debug), the Romi32U4 has been assembled and programmed to drive in a circle. This was completed by modifying the **Romi-NoRpi-Debug.ino** file to set the *_debug_linear_ms* and *_debug_angle_rs* values both to a slow speed.

circle demo: https://youtu.be/laa_JHOGSms




Next, using the same code from before. modifications were made to the **void loop()** function to make the robot drive in a square. This was implemented by incorporating an *int count* and *bool turnTime* variables. The count variable created is used to arbitrarily count up to 200. When reaching this value, an if statement is executed and turnTime is toggled and radial and linear speeds are changed accordingly. It is interesting to see that the errors are not corrected for in this implementation and are compounded as the program executes.

square demo: https://youtu.be/BNFb5nkJgO8