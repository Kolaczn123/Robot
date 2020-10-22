from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
max_linear = 0.19
max_rotate = 0.723
linear_ms = max_linear
rotate_rads = 0.0
count = 0
finalCount = 1500
isTurn = True
laps = 0
finalLap = 10

print("initializing...")
#romi.pixels(0,0,255)

print("begin square...")
i=0
while(True):
	romi.twist(linear_ms,rotate_rads)
	count += 1
	
	if (i == 4):
		i=0
		laps+=1	
		print(f"lap: {laps} / {finalLap}")
		
		
	if (laps == finalLap):
		break
	if (count == finalCount):
		count = 0
		if (isTurn):
			linear_ms = 0.0
			rotate_rads = max_rotate
			isTurn = False
			i+=1
		else:
			linear_ms = max_linear
			rotate_rads = 0.0
			isTurn = True
		


