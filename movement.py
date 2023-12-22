#variable declaration
ACCELERATIONX = 1.3 #Any value above 0
ACCELERATIONY = 1.3 #Any value above 0

FRICTIONX = -0.9 #Any value below 0
FRICTIONY = -0.9 #Any value below 0

MAX_XVEL = 5
MAX_YVEL = 5

THRESHHOLDX = 0.25 #Minimum veloctiy threshhold
THRESHHOLDY = 0.25 #Minimum veloctiy threshhold

def step(velX, velY): #returns the change of position on each frame
    return


def calcVel(velX, velY, inpX, inpY): #Returns the new velocity as a tuple each in-game frame.
                                     #Here, Velx and VelY are the current velcities as a int, float or double
                                     #and inpX and inpY are either -1 for left / up, 0 for neutral and 1 for right / down
                                     #Velocity should be the amount of distance unit the player moves in that frame.
                                     
                                     #NOTE!, negative values for inpX and inpY don't work yet
                                     
    
    if velX <= MAX_XVEL and inpX: #multiply vel with acceleration if moving into diretction
        velX += ACCELERATIONX * inpX
        
    elif inpX == 0 or velX >= MAX_XVEL: #Friction calculation
        velX += FRICTIONX
        
    if velX < THRESHHOLDX: #make player stop moving if velocity is under a certain freshhold
        velX = 0
        
    if velX == 0: #initial velocity
        velX = ACCELERATIONX /2 * inpX


    if velY <= MAX_YVEL and inpY:
        velY += ACCELERATIONY * inpY
        
    elif inpY == 0 or velY >= MAX_YVEL:
        velY+= FRICTIONY
        
    if velY < THRESHHOLDY:
        velY = 0
        
    if velY == 0:
        velY = ACCELERATIONY /2 * inpY

    return(velX, velY)


if __name__ == '__main__':# for testing purposes
    velX = 2
    velY = 1.2
    print("X, !Y")
    print()
    for i in range(22):
        velX, velY = calcVel(velX, velY, 0, 1)
        print(f'XVelocity: {round(velX, 2) } | YVelocity: {round(velY, 2)}')
    
    print("X, Y")
    print()
    for i in range(22):
        velX, velY = calcVel(velX, velY, 1, -1)
        print(f'XVelocity: {round(velX, 2) } | YVelocity: {round(velY, 2)}')
    
    print("!X, !Y")
    print()
    for i in range(30):
        velX, velY = calcVel(velX, velY, -1, 0)
        print(f'XVelocity: {round(velX, 2) } | YVelocity: {round(velY, 2)}')