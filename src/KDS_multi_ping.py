import os
import multiprocessing
import time

def ping(startip, endip):
    IpAddress = str(startip) + str(".") + str(endip)
    print("opening: ", IpAddress, " in cmd")
    os.system('start cmd /k "ping "' + str(IpAddress) + '" -t"')
   
if __name__ == '__main__':
    #jobs = []
    print("Press 1 for 192.168 \npress 2 for 10.46 \npress 3 for 10.47 (Norway) \n")
    option = int(input("Your option : "))

    if option == 1:
        startIp = "192.168"
    elif option == 2:
        startIp = "10.46"
    elif option == 3:
        startIp = "10.47"
    else:
        print("Incorrect option")
        exit()
    restaurantIp = input("Please enter restaurant(Exemple Mall of Scandinavia: 104): ")
    endIp = input("Please enter IP range(Example, 21 or 31 for KDS01): ")
    numberOfSessions = input("Please enter range of windows to open: ")
    for i in range(int(numberOfSessions)):
        #newEndIp = restaurantIp + str(".") + ("%.2f" % (float(endIp) + round(float(i/100),2)))
        newEndIp = str(restaurantIp) + str(".") + str((int(endIp) + int(i)))
        process = multiprocessing.Process(target=ping, args= (startIp, newEndIp))
        #jobs.append(process)
        process.start()
        time.sleep(0.3)