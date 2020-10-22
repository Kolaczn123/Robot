#!/usr/bin/python2
#
# Move the robot forwards and backwards
from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
linear_ms = 0.1
rotate_rads = 0.5
count = 0
finalCount = 48000


print("initializing...")
#romi.pixels(0,0,255)

print("begin circle...")

while(True):
	romi.twist(linear_ms,rotate_rads)
	count += 1
	if (count == finalCount):
		break


