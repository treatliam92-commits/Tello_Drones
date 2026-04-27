# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 10):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nBrennen Koernke & Liam Treat")
print("Program Name: Hoop Competition")
print("Date: 4.20.2026 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('battery?', 2)
        sendmsg('takeoff')


        #Comit message: First hoop - stable - Go - DONE
        #Don't Forget to take video of this portion of the competition
        #Make sure I put the video in our repository
        #Commit message: First hoop video in repository
        #write code below
        sendmsg('forward 150')

        #Comit message: Second hoop - stable - Go
        #Don't Forget to take video of this portion of the competition
        #Make sure I put the video in our repository
        #Commit message: Second hoop video in repository
        sendmsg('go 190 0 50 75')

        #Comit message: Third hoop - stable - curve - negative right positive left
        #Don't Forget to take video of this portion of the competition
        #Make sure I put the video in our repository
        #Commit message: Third hoop video in repository
        sendmsg('curve 140 130 0 0 260 0 40')


        #Comit message: Fourth hoop - stable - Go
        #Don't Forget to take video of this portion of the competition
        #Make sure I put the video in our repository
        #Commit message: Fourth hoop video in repository
        sendmsg('go -190 0 -50 75')

        #Video of Entire hoop competition
        #Comit message: Video of entire Hoop competition in repository

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
