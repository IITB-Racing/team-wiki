# Overview

Our aim:

- Get an optimal track to be followed
- Give throttle/brakes/steering command to the car to follow that path

Algorithms Explored till now :-

- For Steering:
    1. Pure Pursuit Controller
    2. Steering proportional Cross track error
- For Throttle/Brakes:
    1. PID control

## What we did in 2022-23

 Firstly, we mainly worked on the improving only our PPC algorithms by using entire map of cones and the co-ordinates of car given by simulator directly. We tried to obtain the raceline via different methods. The pipelines integration was done in a step by step manner, where-in SLAM+PPC was integrated via fake perception measurements on fsds simulator. 
 We also developed a bot to integrate and test our pipeline. 

#### Path Planning

During planning we try to obtain the waypoint using the global coordiantes of the cones receieved by SLAM. In the first lap, mid-point trajectory is followed. We expect to follow the raceline after the first lap as we have the entire map after the first lap


#### Controls

- Throttle / Brakes  :- A PID controller was used to control the accelerator and braking measurement.
- Steering control :- A pure pursuit controller with varying look ahead vector was implemented to calculate our steering angle

#### What wasn't going well

- The throttle/brakes controller was not actually a PID, the differential term was taken to be the rate of change of the velocity which is theortically not correct but the car still loosely followed the velocity profile.
- Path planning algorithm only worked for entire blue and yellow cones array, and also the closest cones were already matched, i.e. the cones at same index in both the arrays had the same index
- There was no algorithm in place for the first lap of the track when the environment is not known
- Raceline generation takes time. We can't wait after the first lap for the compute to generate the raceline.
- On the fsds simulator, the car always used to hit a cone which might be because of wrong:-
    1. velocity profile generation
    2. throttle/brake controller

written by Deep Boliya