# A fancy little mechanism called the ARP table. The Address Resolution Protocol (ARP) works like this:

# you plug a new device into the network
# it calls out over the broadcast address* and asks “i have a unique identifier** of xy, who has an address for me?”
# The DHCP***server responds to your device and says “here’s an address!” .
# this doesn’t apply if the network has no DHCP server and everything is static.
# The device then uses the broadcast address and yells to the network “hey! My unique identification is xy and my address is xx”
# The ARP table on all listening devices (the whole network) records in their ARP table that the device with unique ID xy is located at address xx.
# The next device that wants to communicate with the first device, uses the broadcast address and says “hey! I want to talk to the device at address xx!”
# The network devices that have record of your IP “xx” will respond and say, the device with IP address xx, is located at unique ID xy”
# The connection is then made, because the devices were told by the switch or router where the other device was.
# That’s all there is to it!

# *broadcast addresses are different for every subnet, that’s an answer in and of itself, for all this answer requires, it’s literally a device yelling “I’m here!”

# **the unique ID is the MAC address. Another story for another day. But the quick and dirty is that every manufacturer is assigned a set of numbers called “OUI”, OUI identifies the manufacturer and the rest of the MAC address is randomly generated or sequential as devices are built. MAC addresses used to be more unique, but as time goes on, the chances for duplicate MACs increase. That does not negate the fact that it is still a unique hardware identifier used to identity devices in the ARP table.

# ***DHCP server stands for dynamic host control protocol and is responsible for assigning addresses to devices that ask for addresses. It has other functions as well, but that will do for this answer.

