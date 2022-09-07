import robot 
from time import sleep 

arlo = robot.Robot()

# print(arlo.go_diff(64,64,1,1))
# sleep(2)
# print(arlo.stop)
# print("finish")

print(arlo.go_diff(64,64,1,-1))
sleep(2)
print(arlo.stop)


# #Rotation?
# print(arlo.go_diff(64,64,1,-1))
# sleep(2)
# print(arlo.stop)

# #Square?
# print(arlo.go_diff(64,64,1,1)) #drive straigt: Start
# sleep(2)
# print(arlo.go_diff(64,64,1,-1)) #turn 1
# sleep(2)
# print(arlo.go_diff(64,64,1,1))#drive straigt
# sleep(2)
# print(arlo.go_diff(64,64,1,-1))#turn 2
# sleep(2)
# print(arlo.go_diff(64,64,1,1))#drive straigt
# sleep(2)
# print(arlo.go_diff(64,64,1,-1))#turn 3
# sleep(2)
# print(arlo.go_diff(64,64,1,1))#drive straigt: Stop
# sleep(2)
# print(arlo.stop)