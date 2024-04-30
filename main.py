from scapy.all import *
import time
import socket
import tkinter

INTERFACE='wlp2s0'

class Device:
    def __init__(self,hostname,mac_address,ip_address):
        self.hostname=hostname
        self.mac_address=mac_address
        self.ip_address=ip_address


all_devices=[];
        
while True:

    curr_time= datetime.now()
    #listen on the interface for network traffic
    a=sniff(iface=INTERFACE,filter="port 67 or port 68",count=1)
    #finding the MAC adress
    mac_address=a[Ether][0].src
    requested_ip_address=""
  
    for opt in a[0][DHCP].options:
        #There's a bunch of information in the DHCP traffic, we just want the
		# information that's presented in a tuple
        if isinstance(opt,tuple):
            address_pair=opt
            #if the option specifies the requested ipaddress, use that as the name
            if address_pair[0]=="requested_addr":
                  requested_ip_address=address_pair[1]

    try: 
        hostname=socket.gethostbyaddr(requested_ip_address)[0]
    except:
        hostname="Unknown"

    device=Device(hostname=hostname,mac_address=mac_address,ip_address=requested_ip_address)
    all_devices.append(device);

    print("{}: {} ({}) has joined your network".format(curr_time, device.hostname, device.mac_address))








#references
    #https://gist.github.com/TheZehn/182b05dfcde4331315c453b63af1a3f9
    #using socket library to try and get the hostname by the assigned IP : https://stackoverflow.com/questions/70056880/is-there-a-way-to-get-hostnames-with-scapy-in-python




















    #----This section doesnt work-------------------------------

    # #Finding the hostname by going through DHCP options
    # for opt in a[0][DHCP].options:
    #     #There's a bunch of information in the DHCP traffic, we just want the
	# 	# information that's presented in a tuple
    #     if isinstance(opt,type):
    #         option,value=opt
    #         #if the option specifies the hostname, use that as the name
    #         if option=='hostname':
    #               hostname=value

  
            
    