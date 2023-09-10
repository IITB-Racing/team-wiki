# Overview 
CAN(Controller Area Network)

- Standard CAN uses an 11-bit identifier for different messages, which comes to a total of 211, i.e. 2048, different message IDs. 
- CAN was later modified; the identifier was expanded to 29 bits, giving 229 identifiers. This is called Extended CAN. 
- CAN uses a multi-master bus, where all messages are broadcast on the entire network. The identifiers provide a message priority for arbitration.

<img src ="https://i.ytimg.com/vi/i5iWAl74Iug/maxresdefault.jpg" width="400" height="150" class="center">

## Working of CAN

The driver's input initially sees a '1' and complements this to a zero, which is placed on CANH. CANL sees the complement of CANH and goes high. Notice that the CANH and CANL voltages are offset from one another. During time t1, CANH – CANL is very close to zero, since CANH and CANL are almost the same voltage. This period, where the driver is sending a logic '1' resulting in CANH and CANL being close to the same voltage, is what we call the CAN recessive state.

<img src ="https://www.allaboutcircuits.com/uploads/articles/6.jpg" width="400" height="150" class="center">


## Priority Arbitration

In a Controller Area Network (CAN), lower 11-bit identifiers indicate higher message priority. Nodes both send and monitor the bus. If a node sends recessive bits (logic '1') but detects a dominant bit (logic '0') on the bus, it backs off. This non-destructive arbitration ensures that higher-priority messages can continue uninterrupted. In essence, recessive bits lose to dominant bits, aligning with lower identifier values indicating higher priority. It guarantees the successful transmission of the highest-priority message while maintaining data integrity.

<img src ="hhttps://www.allaboutcircuits.com/uploads/articles/7.jpg" width="400" height="150" class="center">


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

