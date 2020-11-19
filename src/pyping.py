import os
import multiprocessing

def ping(startip, endip):
    IpAddress = str(startip) + str(".") + str(endip)
    print("opening: ", IpAddress, " in cmd")
    os.system('start cmd /k "ping "' + str(IpAddress) + '" -t"')
   
if __name__ == '__main__':
    #jobs = []
    startip = input("Please enter a start ip example 192.168.1: ")
    endip = input("Please enter a end ip example 31: ")
    numberOfSessions = input("Please enter range of windows to open: ")
    for i in range(int(numberOfSessions)):
        process = multiprocessing.Process(target=ping, args= (startip, int(endip) + int(i)))
        #jobs.append(process)
        process.start()