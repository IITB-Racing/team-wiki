# Overview

## What we did in 2022-23
During 2022-23 we worked on alot of things, few of them are mentioned below:

- Setting up ROS communication between various nodes.
- Researching and setting up CAN communication and socketCAN
- Testing our pipelines on simulators
- Sensor Integration into our algorithm
- The most time consuming of all, solving bt(s) along the way 

**TL;DR:**
Integrated the system


#### Initial Plan 
Our work resembeled our initial plan quite well, with the goal of succesfully running our pipeline together along with sensors. Along with this we planned to include the **[CAN API](https://github.com/FS-AI/FS-AI_API)** provided by FSAI to include in our code for communication with CAN, but instead we used our own python code to do this (discussed under the section of what wasn't going well); we planned to utilise CarMaker (one of the simulator we use) to its fullest potential; we also planned to run our entire pipeline on atleast one of the simulator to produce satifactory results.
The results we obtained looked like this

![image](https://drive.google.com/uc?export=view&id=1CAciOBPM5S7dLc6VeeacMcb87uyFe_Rv)

Here these blue patches are the poition of cones with their variance.

#### What wasn't going well
Well for starters, nothing ever went well (a sentence which seems to be always true for SysInt), the major L's were as follows

-   CarMaker does not publishes the global velocity and yaws of the car, so we had to change the code of the CarMaker node.
-   CarMaker still does not publishes the global coordinates of the cones, instead it defines the position of cones wrt the predefined path (called "route") of the vehicle.
-   CAN communication hardware setup remained a pain in the ass for a long time.

#### Results
WILL ADD PICTURES and VIDEOS

#### The good
~Explain the good things/postive things about the algorithm and/or out implementation of it.~
Not empty by choice

#### The bad
Will Add This Part Later, NGL it would be the major chunk


#### What could be done next?
!<img src ="https://i.imgflip.com/7w3lae.jpg" width="350" height="150">

The moment I begin contemplating potential next steps, I find myself inundated with a deluge of countless creative ideas.

Envisioned for the future are a set of foundational enhancements that merit our diligent attention and efforts:

* Moving onto ROS2 as that seems to be the road ahead, with noetic about to reach its EOL, I see no point in continuing with ROS1 any further. 
<img src="https://global.discourse-cdn.com/business7/uploads/ros/original/2X/a/aba025618280e8de86c49ef47bac2b92523b395f.jpeg" width="350">

* During our talk with different teams in FSAI we found out that there are subdivisions in some teams that have the job of making life easier for the other members, from developing GUIs to automation of ROS to even developing cloud based substitute for GitHub.
* Using CarMaker to its fullest potential, which include testing Jetson with CM communicating through CAN
* Developing our own simulator will be the need of the future, and should be looked into

written by Mohak Vyas