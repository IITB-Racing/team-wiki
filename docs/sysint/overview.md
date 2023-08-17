# Overview

## What we did in 2022-23
During 2022-23 we worked on alot of things, few of them are mentioned below:

- Setting up ROS communication between various nodes.
- Researching and setting up CAN communication and socketCAN
- Testing our pipelines on simulator**s**
- Sensor Integration into our algorithm
- The most time consuming of all, solving bt(s) along the way 

**TL;DR:**
Integrated the system


#### Initial Plan 
Our work resembeled our initial plan quite well, with the goal of succesfully running our pipeline together along with sensors. Along with this we planned to include the [CAN API](https://github.com/FS-AI/FS-AI_API) provided by FSAI to include in our code for communication with CAN, but instead we used our own python code to do this (discussed under the section of what wasn't going well); we planned to utilise CarMaker (one of the simulator we use) to its fullest potential; we also planned to run our entire pipeline on atleast one of the simulator to produce satifactory results.
The results we obtained looked like this

![image](https://drive.google.com/uc?export=view&id=1CAciOBPM5S7dLc6VeeacMcb87uyFe_Rv)

Here these blue patches are the poition of cones with their variance.

#### What wasn't going well
Well for starters, nothing ever went well (a sentence which seems to be always true for SysInt), the major L's were as follows

-   CarMaker does not publishes the global velocity and yaws of the car, so we had to change the code of the CarMaker node.
-   CarMaker still does not publishes the global coordinates of the cones, instead it defines the position of cones wrt the predefined path (called "route") of the vehicle.
-   CAN communication hardware setup remained a pain in the ass for a long time.


#### How we tried to resolve it

#### Results
Explain how did we measure the results, and what were the results we got. Do share pirctures of them.

#### The good
~Explain the good things/postive things about the algorithm and/or out implementation of it.~

#### The bad
Explain any shortcomings/issues with the algorithm and/or our implementation of it.


#### What could be done next?
!<img src ="https://i.imgflip.com/7w3lae.jpg" width="350" height="150">

The moment I begin contemplating potential next steps, I find myself inundated with a deluge of countless creative ideas.
Here are some basic upgrades that we should be working on in the future:
* 

