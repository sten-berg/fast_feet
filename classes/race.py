from driver import drivers
from track import spaFrancorchamps
import time
import random



def driverProgress():
    for driver in drivers:
        driver.setPosition(random.randrange(0,10))
        if driver.getPosition() >= spaFrancorchamps.getFinish():
            #print("Comparing driver.getPosition with spaFrancorchamps.getFinish")
            driver.setLap()
            driver.setLapTime(0)
            #print("modulus: " + str(driver.getPosition() % spaFrancorchamps.getFinish()))
            driver.setPosition( -50 + (driver.getPosition() % spaFrancorchamps.getFinish()))
            if driver.getLap() > 2:
                print('Winner of the ' + spaFrancorchamps.getName() + ' Grand Prix, is: ' + driver.getName())
                exit()

def driverStatus():
    for driver in drivers:
        print(str(driver.getName()) + ' is on lap: ' + str(driver.getLap()))
        print(str(driver.getName()) + ' is on position: ' + str(driver.getPosition()))

def init():
    
    while True:
        time.sleep(1)
        driverStatus()
        driverProgress()


    


init()
