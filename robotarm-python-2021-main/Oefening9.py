from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')   

# Jouw python instructies zet je vanaf hier:
for x in range(1,5):
    for i in range(0,x):
        robotArm.grab()

        for a in range(0,5):
            robotArm.moveRight()
        robotArm.drop()

        for b in range(0,5):
            robotArm.moveLeft()

    robotArm.moveRight()