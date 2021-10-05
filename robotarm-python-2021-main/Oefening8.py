from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for x in range(7):
    robotArm.grab()
    for i in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(8):
        robotArm.moveLeft()
robotArm.wait()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()