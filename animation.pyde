xCoordinate = 50
speed = 2
ellipseSize = 20
yCoordinate = 50
yspeed = 2
def setup():
    size(500, 500)
    
def draw():
    background(255,255,255)
    global xCoordinate, speed, ellipseSize
    leftTopBoundary = ellipseSize / 2
    rightBottomBoundary = 500 - ellipseSize / 2
    
    #fill(0, 0, 255)
    #rect(xCoordinate, 50, 40, 40)
    fill(0, 255, 0)
    xCoordinate += speed
    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        speed = -speed
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary:
        yspeed = -yspeed\
        xCoordinate += speed
        yCoordinate += yspeed
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)

    

    
