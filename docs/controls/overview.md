# Overview
Here we need to explain breifly (focus on future plans):

- what stage of the algorithm development we are in and what we are trying to achieve (no need to explain basics)
- what we have done till now and major issues encountered
- what we are planning to do next

## What we did in 2022-23

 Firstly, we mainly worked on the improving only PPC by using entire map of cones and the co-ordinates of car given by simulator itself. We tried to obtain the raceline via different methods. The pipelines integration was done in a step by step manner,where-in SLAM+PPC was integrated via fake perception measurements on fsds simulator. 
 We also developed a bot to integrate and test our pipeline. 



### Path Planning

Using the entire array of blue and yellow cones given by fsds, the midpoint of cones was taken where the the closest blue cone and the yellow cone had the same index and the mid-point trajectory was generated by joining those midpoints by bezier curves.


To generated the raceline, the tracked was divided into sections where a way point lied whose location was goverened by a parameter alpha. After this two things could have been done:
1)Use the lap time as the objective function itself 
2)Use the sum of curvatures at discrete points on the track

Complexity of method 1 was much higher because for a given set of parameters(alphas), we had to interpolate, generate corresponding velocity profile, get distances between all the waypoints, the divide each distance by the velocity on that points. 
Hence method 2 was used, which gave us very good and satisfactory results. 


#### What wasn't going well

The array receieved by fsds has same index, so matching blue and yellow cones was not a problem. In real scenerio, this will not be the case because cones much further ahead can be encountered by pereception and hence this method will not work.

The velocity profile generated was not correct, because while running only ppc code on the training map, the car always used to hit some cones at the very end of the lap

##### How we tried to resolve it

This was resolved by matching the yellow cones with the closest blue cone out of all the blue cones. And if the distance between closest blue cones was more than a certain threshold, no matching was done. 

The velocity profile generated wasn't wrong theoritically. After appling



#### Results
Explain how did we measure the results, and what were the results we got. Do share pirctures of them.

### Controls

#### Acceleration / Braking
A PID controller was used to control the accelerator and braking measurement.
This controller initially being tuned wasn't actually a PID control because it took the previous output of the control loop as a parameter rather than the previous error while trying to follow a velocity profile. And a differentiator on the output prevented the accelerator from clipping keeping the cra slow and hence even after a wrong implementation of the controller, the car stayed on track.



#### Steering control
Explain any shortcomings/issues with the algorithm and/or our implementation of it.

#### Challenges faced
Explain any challenges we faced while implementing the algorithm.

#### What could be done next?
- Delaunay triangulation for path planning in the first lap
- Stanley controller for steering


## Algorithms explored till now
List the algorithms/libraries we have explored till now, and give a breif description of each's implementation, the postives/negatives.

#### Path Planning 
- Midpoint trajecotory
- Raceline trajectory


#### Controls
- PID control for braking/accelerating
- Pure pursuit algorithm for steering