import os
import multiprocessing
def default():
    print("invalid option")
    
def ping(startip, endip):
    IpAddress = str(startip) + str(".") + str(endip)
    print("opening: ", IpAddress, " in cmd")
    os.system('start cmd /k "ping "' + str(IpAddress) + '" -t"')
   
if __name__ == '__main__':
    #jobs = []
    #startIp
    print("Press 1 192.168.1 \npress 2 for 10.46.1 \npress 3 10.47.1 (Norway) \n")
    option = int(input("Your option : "))

    if option == 1:
        startIp = "192.168"
    elif option == 2:
        startIp = "10.46"
    elif option == 3:
        startIp = "10.47"
    else:
        print("Incorrect option")

    #startIp = input("Please enter a start ip example 192.168.1: ")
    endIp = input("Please enter a end ip example 31: ")
    numberOfSessions = input("Please enter range of windows to open: ")
    for i in range(int(numberOfSessions)):
        process = multiprocessing.Process(target=ping, args= (startIp, int(endIp) + int(i)))
        #jobs.append(process)
        process.start()