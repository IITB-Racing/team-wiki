# Overview 
CAN(Controller Area Network)

- Standard CAN uses an 11-bit identifier for different messages, which comes to a total of 211, i.e. 2048, different message IDs. 
- CAN was later modified; the identifier was expanded to 29 bits, giving 229 identifiers. This is called Extended CAN. 
- CAN uses a multi-master bus, where all messages are broadcast on the entire network. The identifiers provide a message priority for arbitration.


<img src ="https://i.ytimg.com/vi/i5iWAl74Iug/maxresdefault.jpg" width="400" height="150" class="center">


## What we did before the competition

- Used Virtual CAN in linux to decode and check CAN transmission using FSAI .dbc file.
- Established CAN communication of ECD board with Jetson using USB-CAN converter in Linux using Arduino IDE

## What we did during the competition
- Had to use InCarPc as Jetson did not work and replaced the CAN cable to PCAN to resolve transmission issues
- Used the Cantools library in python to make our API which interfaces with the car 
- Wrote the inspection and Autonomous demo codes which is required before participating in any dynamic event
- Inspection codes went well but in the autonomous demo we had to turn steering left right and then center which we missed!!

## Challenges Faced

## Plan ahead
Describe the tasks to pe performed in this year

