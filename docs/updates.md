# Weekly priorities

### Feb 5- Feb 14

**Oreo / Recruitment**

- [x]  **DV oreo presentation**
- [ ]  **Paper checking - Feb 14 raat tak**
    - assign 10-10 questions to each jde…

**BOT**

- [ ]  **Collect data on accel like track ⇒ test Perc + SLAM @Ayush Rohilla @Deep Boliya**
    - everything is now set-up, we should be able to collect data now ⇒ tom: @Deep Boliya @Ayush Rohilla
    - imu usb to rs-232 cable is missing, search / buy new one: connect with their support
- [ ]  test ppc on bot:
    - change output of code  to voltages - @Deep Boliya

**PPC**

Shubham / Ajinkya

- [ ]  **ROS2 & EUFS installation - Fri**
- [ ]  **Delaunay vs mid-point quantitative study**

Ayush M.

- [x]  **table bnado:** event wise path planning & control algo perf (fill in with comments like: best till now, didn’t try yet, buggy, completes but hitting two cones, relatively more jerky, smooth, etc.)

| Event / Algo | Midpoint-Pure Pursuit | Midpoint-Stanley | Delaunay-Pure Pursuit | Delaunay-Stanley |
| --- | --- | --- | --- | --- |
| Acceleration | working: best till now no cones hit 21 s | haven’t checked | NA | NA |
| Skidpad | not used but can be implemended | working but hitting 2 cones and taking time as throttle is .2 with time of 3 minutes | No need to use delauny as the position of cones is already given | No need to use delauny as the position of cones is already given |
| Autocross | working :best till now 2 hits ,less jerky outputs , 2 cones were hit with time of 56.7 s | no hits but very slow as throttle is .2 very jerky outputs without pid 2.40 minutes | 55 secs | @shubham best for first lap… |
| Trackdrive: optimized lap | only this is working. more than 10 cones hit. time 38 sec | working on it | 32 seconds | N.A |

can use catmull interpolation for skidpad event but not for optimized track and in autocross too at for throttle greater than .2 stanley is not working need to tune it.

- [ ]  pure-pursuit vs stanley: done
    - **raceline pe stanley nahi chalra 5 din se (review @Deep Boliya)**

Deep

- [ ]  **Figure out middle fully on EUFS… @Deep Boliya**
- [x]  **All BOT STUFF…**

**Perception**

- [ ]  **EUFS mono parameters recalculate // all yellow cones available @nakul @Ayush Rohilla (Feb 6)**
    - yellow cones nahi aarha… ⇒ retrain with eufs data (accel bag) **annotate karna hai abhi 67/119**
    - then tune parameters using true depth vs height - aaj hi hojayega (ggs)
- [x]  **tabulate latencies of sub-parts of lidar-fusion forward (10min.)**

| sub-part | time taken |
| --- | --- |
| ground removal | 0.045 |
| clustering | 0.16 |
| transformation | ~0 |

- [ ]  **reverse lidar-fusion (before Feb 10th) @yasht @rajit @abhimanyu**
    - almost done: **Fri tak hojana chahiye**
- [ ]  **transformation bt?**

**SLAM**

- [ ]  **evaluation parameters go-through again → test on mrpt @rohan (Feb 7/8)**
- [ ]  data association:
    - **ICNN almost working: need to sort some errors + test on rviz (Feb 6/7) @amna**
        - fri night will start → sat tak
    - **review localization code @Ayush Rohilla @shreyash Gupta - FRIDAY**

**Sys-int**

- [x]  mrpt with ros1-bridge: @vishwam
    - ~~mrpt_msgs pkg ke msgs not in rosmsg list; try using ros1 branch of mrpt-msgs (10min)~~
    - **~~preparing fake perception node (done by Bhaskar): need to test~~**
    - ~~running mrpt on eufs accel bag~~
- [ ]  eufs sim dev:
    - **sensor position finalize: discuss with perc where best position for lidar & zed cam @Yash Rampuria @Mohak Vyas (Feb 6)**
        - should we make a cart that duplicates these positions, and then collect data on it (I saw one team doing this)
        - use eufs to experiment: eufs_ws/src/eufs_sim/eufs_racecar/robots/ads-dv/robot.urdf.xacro
        
        | Sensor | Options | Remarks |
        | --- | --- | --- |
        | LiDAR | ekdum front (tilted upwards?) | + amz, front seems better coz no points from car + zyaada range - vibrations zyaada ayenge? |
        |  | upar (tilted downwards) | oxford on ads-dv, Edinburgh |
        | Stereo cam | upar only one |  |
        |  | upar with two stereo | Edinburgh |
        |  |  |  |
    
    - **~~understanding eufs_sim: https://gitlab.com/eufs/eufs_sim/-/wikis/Design-Overview @bhaskar (Feb 11/12)~~**
    - **vehicle dynamics of real ads-dv: figure out vehicle parameters design… give to chandu send CAD + … @Ayush Rohilla @chandra mouli (Feb 7)**
        - https://github.com/FS-AI/FS-AI_ADS-DV_CAD

---

- [ ]  velocity controller first lap not using PID (throttle brake)
    - can use aage ke 4 points for PID instead of full-path
- [ ]  Watching control systems playlist till

    [Basics of Control Systems | Chapter-1 | Control Systems](https://youtube.com/playlist?list=PLBlnK6fEyqRjQIKIbGFAopRhZ1mNSv0pM&feature=shared)

- [ ]  comparative study: time based optimization:
    - curvature based almost done // time optimized makes more sense…
    - getting some issue with SciPy-lab
- [ ]  transition code from first lap → optimized path

- [ ]  transition code (on the way parallelly karna)
    - implementation not started
    
- [ ]  JCBB similar errors, can get sorted 3-4 days after ICNN gets sorted

- [ ]  eufs sim dev:
    - integration of the vehicle interface with simulated vehicle actuator controller(s)
    - different graphs/plots like in AMZ’s CI/CD platform
    - server ka jugaad (profs / aws free plans) since rosbag bazaar is open-source by amz https://github.com/AMZ-Driverless/rbb_core
    - driver model: https://www.degruyter.com/document/doi/10.1515/auto-2022-0097/html?lang=en
- [ ]  CM11 download check?… (for running: mono + middle + mrpt)


### Oct 10 - Oct 17 [13/33 = 39.39%]

- **Sim dev setup in Carmaker** @Mohak Vyas
    - github repo setup — [P0 !!] **(blocking!)** ❌
        - should be able to launch carmaker easily - CM to alag se hi open karna padega ✅
        - change topic names to common topic names chosen ❌
        - launch file for acceleration ❌
        
        perception code missing, slam + ppc chala skte hain rn
        
        then try perception (as in fsds)
        
    - acceleration map ready — [P0] **(blocking!)** ❌
    - ask in forums: — [P1] ✅
        - lidar in CM?
        - road pe white stripes?
        - cones ke white stripes?
        
        Road pe white stripes / cone ke white stripes is sorted. Lidar isn't on CM yet, they'll be releasing it in the new version, to be realeased soon in Oct'23... 

    - able to get ground truth info (cones/car location, speed, …) — [P1] ✅

- **Acceleration ~~in carmaker~~** @Deep Boliya @Mohak Vyas
    
    <u>goal: to complete under 5 sec in simulations</u>
    
    - improving accel based on to-dos — [P0] **(blocking!)** ✅
        - [x]  clamp steering (not do too much steering at any time) (ya to extreme case nahi aayega, ya recover nahi hoga)
        - [x]  autocross ke liye try karle
        
        **best result we’re getting rn is ~8sec**
        
    - port → carmaker — [P1] ❌
    - start impelementing ‘alternate ways’ — [P1]
        1. FSDS: seeing first few cones & interpolating to get boundary paths @rajit @ayush 
            1. to stay within boundary, we’ll need to know our location → use odometry
                1. interpolation with first few cones while gaadi static ✅
                2. implement tue controller ❌
            2. initial cones might not be accurate enough → lines might not be very straight ❌
                - [ ]  plot in rviz to test this

- **Skidpad execution**
    
    <u>goal: to complete under 20 sec in simulations</u>
    
    current to dos:
    
    - make ppc code for this, same in both cases (try with/without error in car state) @ajinkya ❌
    - make slam/localization code ready, & try with known cone positions @arnav ❌
    
    furhter to dos:
    
    - try with mrpt, cones location unknown @Shreyash Gupta ❌

- **Perception specific**
    - able to run from a launch file (fix path error) @Yash Rampuria — [P0] **(blocking!)** ✅
    - researching on how to: @Yash Rampuria — [P0] ✅
        - improve range in stereo/mono pipeline? → using lidar
        - improve latency in mono pipelines? → nn / mono (sift paused)
    - using nueral network: @tangri — [P1] (avg error % = 4.15%) ✅
    - training a neural network to find depth using bounding boxes data @rajit — [P1] ✅
        - rn getting avg error % = 5.2% → scope for improvement
            
            **but how much should error should we aim for? → run slam + ppc, with fake_meas + noise to check for this ig…?**
            
    - lidar pipeline: @nakul — [P1] ❌
        - talk to @namitha?
        - code chal rha hai, transformation matrices not correct probably, trying to fix it through calibration via matlab
        
        currently working on prev DEs ke code, fixing many errors… (not sure if transformation matrix is right)
        
    - yolo retraining: @abhimanyu — [P1] sensors (zed / lidar) launch nahi hote everytime, bt dete h;ain mostly ✅
        - blue/yellow cones ko bg classify kar rha hai - esp for far cones → will need more training with colab
        - get help from @amit-sethi on training
        
        getting better results, **orientation thresholds change karne hain**
        
    - ~~sift on gpu @rajit — [P0] **(halted)**~~
        - oct 11: zed, cuda sab installed!
    
    !!! note
        ❓ Mono giving different sizes of bounding box for one side → some bias in depth → perception + slam: deviating from straight. @Yash Rampuria what are we doing about this?? — retraining mono
        
        also sensors (zed / lidar) launch nahi hote everytime, bt dete hain?
    

- **Slam specific**
    - root cause for data association issue (in fsds, with fake meas) — [P0] @Shreyash Gupta ✅
        - update/correct full code according to a single ref **by sunday** **(blocking!) (~1din aur)**
        - do a very structured root cause analysis
    - graphslam @Shreyash Gupta @rohan — [P1]
        - start writting some code for… (what should we aim for initially?) ✅
            - include hone mein BT
            - example code is running
        
        **now onto how we can use that with out problem**
        
    - ~~porting fastslam → carmaker @Shreyash Gupta @arnav — [P1]~~
    - connecting perc to slam @rajit — [P1] ❌
    - better velocity estimation / odometry estimation method @amna — [P1] ❌
        - figuring out how to implement - need to learn KF? (as no direct implementation details)
        - started implementing: (doubtful if we want to continue this further)
        
        [](https://github.com/sharathsrini/Kalman-Filter-for-Sensor-Fusion/blob/master/README.md)
        

- **PPC specific**
    - reading on mpc @Deep Boliya
        - reading the math behind: it is an optimization problem ✅
        
        need more time to start implementing
        
    - get & understand psuedo-transient model from @chandu @Deep Boliya ❌
    - implement Pure pursuit @shubham
        
        controller bacha hai ~1day
        
    - implementing delaunay triangulation @shubham ❌
    - complete stanley implementation @ajinkya @ayush ❌
        - code likh liya hai for stanley, but error hai, starting mein right le rha hai
        - oct 15: straight jaa rha hai but turn nahi le rha - ajinkya (knows root cause)
        - cross error minimising → to the other side - mishra (knows root cause)

- **Sys-int specific**
    - able to run iitbdv repo, with docker, on fsds rosbag (mono, mrpt, middle/raceline + accel) @bhaskar **(blocking!)** ✅
        - on rosbag
        - github actions → on push check if everything is building correctly
    - explore CAN in carmaker @MG @vishwam ❌
        - **ya to transfer deep → vishwam, aur liscense need ask @Ayush Rohilla** ✅
    - exploring: how to make our own simulator @MG @bhaskar ❌
    
        [eufs sim package documentation](https://docs.google.com/document/d/10D429wQYfawIpyEiWkgNUOZKX_tankgkixVVAmSiZaA/edit)

    - ~~sorting out github pull actions~~ + branch structure @MG
    
    !!! note
        ❓ **Lidar not on CM is a biggggg bt, should we be looking for backup in case CM delays their update?   ** @Mohak Vyas
    

- **Jetson** — [P0]
    1. not booting up, try reinstalling / force recovery mode ubuntu **(blocking!)** ❌

- **Team wiki completion** — [P2]
    - **Perception:** incorporate the feedbacks, more pages? @Yash Rampuria ❌ 
    @abhimanyu karega ab
    - **SLAM:** complete MRPT page @Shreyash Gupta ❌
    ye to shreyash to hi karna padega
    - **Sys int:** incorporate the feedbacks, more pages (simulatation, bot), ~~docker @bhaskar~~ @Mohak Vyas @MG ❌

- **Ideation on Trainee modules** - [P2]
    
    Recruitment might start late. Need a different/structured recruitment + trainee module plan so that:
    
    - reach more freshers, when we’re starting recruitment late?
    - min effort by team (a lot of time/effort goes for debugging errors / installing in the modules)
        - structured week-by-week content with assignments documented on docs / github
        - meeting with trainees one time a week?
    - a good efficient outcome (we gave 4 months, but they still some have installation issues + need to more training to be able to contribute to their subsystem).
        - should we spend less time in modules, and make JDEs faster so they’ve more time to learn their subsytems?
    - how to improve SLAM module? - no first pref till now ☹️
    
    **to do:** need to work on the overall structure and req. / what changes can be made @Ayush Rohilla ❌
    

- **Open questions**
    1. **what all data (& where) do we’ve collected from ads-dv from last season?**
        1. 5 accel
        2. 2 zig zag
        
        pen drives mein hai but online nahi upload kar skte…
        
        **need to buy a hard drive compatible with in-car pc**: https://github.com/FS-AI/FS-AI_Compute/issues/1
        
    2. do we know what was going wrong ab tak in meas_update? 
        
        probably kaafi mix match tha logic mein, even le large had some error in their code

### Oct 2 - Oct 9 [7/30 = 23.33%]

- **Sim dev setup in Carmaker** @Mohak Vyas
    - github repo setup — [P0 !!] **(blocking!)** ❌
        - should be able to launch carmaker easily
        - change topic names to common topic names chosen
        - launch file for acceleration
    - acceleration map ready — [P1] **(blocking!)** ❌
    - ask in forums: — [P0] ❌
        - lidar in CM?
        - cones/road pe white stripes?
    - able to get ground truth info (cones/car location, speed, …) — [P1] ❌

- **Acceleration in carmaker** @Deep Boliya @Mohak Vyas
    
    goal: to complete under 5 sec in simulations
    
    ![Acceleration track](accel.png)
    
    *<center>(For FSAI: 0.3m from starting line, 75m track length, 3m wide, 100m stopping length)</center>*
    
    - improving accel based on to-dos — [P0] ✅
        - [x]  tuning the pid
        - [x]  improving controller → differential one
        - [ ]  clamp steering (not do too much steering at any time) (ya to extreme case nahi aayega, ya recover nahi hoga)
        - [x]  start mein teda krke chala ke dekho…
        - [ ]  autocross ke liye try karle
    
    - start impelementing ‘alternate ways’ — [P1] ❌
        1. FSDS: seeing first few cones & interpolating to get boundary paths @rajit @ayush
            1. to stay within boundary, we’ll need to know our location → use odometry
            2. initial cones might not be accurate enough → lines might not be very straight
                - [ ]  plot in rviz to test this
    - port → carmaker — [P1] ❌

- **Skidpad ideation**
    
    goal: to complete under 20 sec in simulations
    
    ![Skidpad track](skidpad.png)
    
    *<center>((FSG’22) The foremost part of the vehicle is staged 15m before the timekeeping line. Pehle right - second lap on right turn is timed. Then left turn - fourth lap on left is timed. must come to a full stop within 25m after crossing the timekeeping line)</center>*
    
    - come up with ways we can complete skidpad — [P0] @Ayush Rohilla @DEs ✅
    !!! note
        - assuming the map is placed as per the diagram:
            - perc: mono / best pipeline (as bohut saare cones ek saath, time le skta hai to compute)
            - slam: **ekf localization to be figured out @Shreyash Gupta — hai ek library with feature map option…**
            - ppc: we know the boundaries either way, so we’ll know what middle path to follow
        - assuming the map isn’t placed as per the diagram (but boundaries same):
            - perc: same
            - slam: try with mrpt, range ~15m;
                
                can we alter the meas coming in so that cones given by perception always lie on boundary? sounds fishy.
                
            - ppc: same
        
        next to-dos:
        
        1. make ppc code for this, same in both cases (try with/without error in car state) @ajinkya 
        2. try with mrpt, cones location unknown @Shreyash Gupta 
        3. make slam/localization code ready, & try with known cone positions @arnav

- **Perception specific**
    - able to run from a launch file (fix path error) @Yash Rampuria — [P0] **(blocking!)** ❌
    - researching on how to: @Yash Rampuria — [P0] ❌
        - improve range in stereo/mono pipeline?
        - improve latency in mono pipelines?
    - using nueral network: @tangri — [P0] ❌
    - lidar pipeline: @nakul — [P1] ❌
        1. Find u v of a cone centre approximately and using step 3 ka result, find corresponding depth: ~2-3 days ✅
        2. nan values error → last year code lookup; ~2-3 days (nakul ka code, not continuing) 
        3. talk to @namitha?
        
        currently working on prev DEs ke code, fixing many errors… (not sure if transformation matrix is right)
        
        working on: we’ll take depth from lidar + use cam for classification (not only lidar pipeline…)
        
    - yolo retraining: @abhimanyu — [P1] sensors (zed / lidar) launch nahi hote everytime, bt dete hain ❌
        - blue/yellow cones ko bg classify kar rha hai - esp for far cones
        - same cone pe do bounding boxes → non-max suppression threshold change (v5 pe hat gye the) ✅
        - will try yoloV8: more stable → thode better results → have to train on better resolutions on colab ✅
        - get help from @amit-sethi on training
        
        will need more training with colab
        
    - sift on gpu @rajit — [P0] **(blocking!)** ✅
        - zed, cuda sab installed!
    
    !!! note
        ❓ Mono giving different sizes of bounding box for one side → some bias in depth → perception + slam: deviating from straight. @Yash Rampuria what are we doing about this?? — retraining mono
        + sensors (zed / lidar) launch nahi hote everytime, bt dete hain
    

- **Slam specific**
    - root cause for data association issue (in fsds, with fake meas) — [P0] @Shreyash Gupta ❌
        - update/correct full code according to a single ref **by sunday** **(blocking!) (~1din aur)**
        - do a very structured root cause analysis
    - graphslam @Shreyash Gupta @rohan — [P1]
        - figure out g2o & graphslam implementation (g2o, …?) ✅
            - understanding the example slam2d
            - what is input & output format????
        - start writting some code for… (what should we aim for initially?) ❌
            - include hone mein BT
        - lelarge waala paper padh le - compares ekf slam vs graphslam ✅
            
            [EKF SLAM vs GraphSLAM](https://www.notion.so/EKF-SLAM-vs-GraphSLAM-41f0f9b07bcc47b5a0003e71c670d024?pvs=21)
            
    - ~~porting fastslam → carmaker @Shreyash Gupta @arnav — [P1]~~
    - connecting perc to slam @rajit — [P1] ❌
    - better velocity estimation / odometry estimation method @amna — [P1] ✅
        - rnn ****1layer vs 2layer, **mkf** with sensors: mkf is best, rnn 1layer is similar
        - rnn 1 layer: motor encoder, **two imu (?)**, gnss
        - mkf.. ke sensors?
        
        struggling to get implementation details
        

- **PPC specific**
    - get & understand psuedo-transient model from @chandu @Deep Boliya ❌
    - plan on delaunay triangulation @deep ✅
        - implementing @shubham
    - Complete stanley implementation @ajinkya @ayush ❌ ~2 days
        - code likh liya hai for stanley, but error hai, starting mein right le rha hai
    - ~~get fsds working with ros bridge~~ and implement Pure pursuit @shubham ❌
    - ~~get fsds working, core dumped @ayush **(blocking!)**~~
    
    !!! note
        📌 JDEs trying to implement ppc without looking into code, interpolating + stanley controller + vel profile / pure-pursuit ~ 3-4 more days. They’re coming with some new ideas to implement.
    

- **Sys-int specific**
    - able to run iitbdv repo, with docker, on fsds rosbag (mono, mrpt, middle/raceline + accel) @bhaskar **(blocking!)** ❌
        - figuring out gui in ros docker ✅
        - figure out how to sync docker files/images?? - does whole 14gb docker image get → only parts, not whole ✅
        - kaburnates… managing docker files? (for multiple docker) ✅
        - on rosbag
        - github actions → on push check if everything is building correctly
    - explore CAN in carmaker @MG @vishwam ❌
        - **ya to transfer deep → vishwam, aur liscense need ask @Ayush Rohilla** 
    - exploring: how to make our own simulator @MG ❌
    
    !!! note
        ❓ carmaker: cone ke white stripes nahi hone chahiye, road ke white stripes se interfere (have cone models with black stripes) @Mohak Vyas. Will we be able to do this? — **ask on forum**
    

- **Jetson** — [P0] ❌
    1. not booting up, try reinstalling / force recovery mode ubuntu @Mohak Vyas @vishwam **(blocking!)**

- **Team wiki completion** — [P2] ❌
    - **Perception:** incorporate the feedbacks, more pages? @Yash Rampuria
    - **SLAM:** complete MRPT page @Shreyash Gupta
    - **Sys int:** incorporate the feedbacks, more pages (simulatation, bot) @Mohak Vyas @MG

- **Ideation on Trainee modules** - [P2] ❌
    
    Recruitment might start late. Need a different/structured recruitment + trainee module plan so that:
    
    - reach more freshers, when we’re starting recruitment late?
    - min effort by team (a lot of time/effort goes for debugging errors / installing in the modules)
        - structured week-by-week content with assignments documented on docs / github
        - meeting with trainees one time a week?
    - a good efficient outcome (we gave 4 months, but they still some have installation issues + need to more training to be able to contribute to their subsystem).
        - should we spend less time in modules, and make JDEs faster so they’ve more time to learn their subsytems?
    - how to improve SLAM module? - no first pref till now ☹️

React 🏎️ to the whatsapp msg, if you’ve carefully read & acknowledged the priorities for this week.

### Sept 26 - Oct 1 [12/27 = 44%]

- **Sim dev setup in Carmaker** @Mohak Vyas ❌
    - github repo setup — [P0 !!]
        - should be able to launch carmaker easily
        - change topic names to common topic names chosen
        - launch file for acceleration
    - able to get ground truth info (cones/car location, speed, …) — [P0]
    - acceleration map ready — [P0]

- **Acceleration in carmaker** @Deep Boliya
    
    0.3m from starting line, 75m track length, 3m wide, 100m stopping length
    
    - list alternative ways to complete acceleration — [P0] ✅
        1. seeing first few cones & interpolating to get boundary paths
            1. to stay within boundary, we’ll need to know our location → use odometry
            2. initial cones might not be accurate enough → lines might not be very straight
                - [ ]  plot in rviz to test this
        2. using Lidar
        3. only orientation
            1. based on assumption that car is staged centered + we can get accurate yaw for a while from imu

    - bearing method (fix the stopping position, Thu night) → carmaker — [P0] ✅
        - what are possible wrong outcomes, with this implementation?
        - on ads-dv will need to aim for an ideal speed to follow, such that pts max + are able to stop safely within 100m (depends on the stopping potential)
        
        !!! note
            🚀 FSDS mein:
            
            - speed 4ms se zyaada nhi
            - off track jaate hi gone case
            - can we use orientation of car to further improve this??
            - using total distance travelled as stopping logic… assuming distance from encoder data to be pretty acurate (as per deep’s experience with ADS-DV), if ads-dv isn’t giving accurate distance tune it there to go more than 75m or less than 75m as req…
            

            **further to dos:**

            - start mein teda krke chala ke dekho…
            - AS_FINISH logic, and successfully return ‘AS_FINSIH’ on terminal - can be done when we port → Carmaker
            - tuning the pid
            - improving controller → differential one
            - clamp steering (not do too much steering at any time) (ya to extreme case nahi aayega ya recover nahi hoga)
            - weighted sum with orientation (not much weight)
            - if off track: yellow/blue identify karke make a turn (if speed is enough, we might not have enough time to see all yellow & deicide to make a turn)
        
    - start impelementing ‘alternate ways’ — [P1] ❌

- **Perception specific**
    - able to run from a launch file (fix path error) @Yash Rampuria — [P0] ❌
    - researching on how to: @Yash Rampuria — [P1] ❌
        - improve latency in mono pipelines?
        - improve range in stereo/mono pipeline?
    - lidar pipeline: @nakul @abhimanyu — [P1]
        1. Put the transformation matrix in a variable as a multiplication of 3 4 different transformations (exteinsic intrinsic etc) ✅
        2. Learn how to read pcd data ✅
        3. Pcd has data in the format (x y z I) and u need to convert it to (u v depth) ✅
        4. Find u v of a cone centre approximately and using step 3 ka result, find corresponding depth - ~ 2-3 days ❌
    - sift on gpu @rajit - driver error ❌
    
    !!! note
        ❓ Mono giving different sizes of bounding box for one side → some bias in depth → perception + slam: deviating from straight. @Yash Rampuria what are we doing about this??
    

- **Slam specific**
    - root cause for data association issue (in fsds, with fake meas) — [P0] @Shreyash Gupta ❌
    - graphslam: come up with a plan @Shreyash Gupta @rohan — [P1]
        - collect resources ✅
        - get overview of the algo ✅
        - examples on how it can be implemented (g2o, …?) ❌
    - porting fastslam → carmaker @Shreyash Gupta @arnav— [P1] ❌
    - better velocity estimation method @amna — [P1] ❌
    - ~~porting mrpt → carmaker??? (ho rakha hai)~~

- **PPC specific**
    - @Deep Boliya to add jde tasks for this week ❌
    
    !!! note
        📌 JDEs trying to implement ppc without looking into code, interpolating + stanley controller + vel profile / pure-pursuit ~ 3-4 more days. Through this they’re coming with some new ideas to implement.
    

- **Sys-int specific**
    - ros2 karna hai ki nahi? (~1-2 din mein decide) — [P1] @Mohak Vyas ✅
        
        nahi for now: faaltu bt nhi lena hai / ros2 has a better way to send msgs than ros1 (less delays due to truely parallel architecture) / ros1 noetic eol in 2025, have two years atleast / we’re all familiar with ros1, will take some to get used to ros2 as well
        
    - docker: plan for integrating (~1-2 din) — [P0] @MG @jdes ✅
        - what should the final output be like?
            
            (what all will it ‘contain’? system requirements, probably require nvidia graphic cards?)
            
        - things the docker should contain 
        https://docs.google.com/document/d/1ojJ-bONWIKGVy3xhxL1UiQXZqVMYcOj-czewkg0QXAo/edit
    
    !!! note
        ❓ carmaker: cone ke white stripes nahi hone chahiye, road ke white stripes se interfere (have cone models with black stripes) @Mohak Vyas. Will we be able to do this?
    

- **Jetson** — [P0]
    1. not booting up, try reinstalling / force recovery mode ubuntu @Mohak Vyas ❌
    2. reach out to nvidia/help center/… @Ayush Rohilla ✅
        1. reaching out through forums - suggesting same, that we should reflash our board with sdkmanager from another x86 host
            
            https://forums.developer.nvidia.com/t/jetson-agx-orin-not-booting-up/267798
            
        2. trying force recovery mode - 
            
            https://forums.developer.nvidia.com/t/agx-orin-not-booting/258038
            

- **Team wiki completion** — [P1]
    - **Perception:** incorporate the feedbacks, more pages? @Yash Rampuria ❌
    - **SLAM:** complete MRPT page @Shreyash Gupta ❌
    - **Sys int:** incorporate the feedbacks, more pages (simulatation, bot) @Mohak Vyas @MG ❌
    - **Overview:** home, goal & vision 2024, ~~compi 101~~, ~~culture?~~ @Ayush Rohilla ✅
    - Local to web, using github hosting, (any method to keep it private!??) @Ayush Rohilla ✅
        - github host from org - not possible, with a personal account, public repo - host possible
            
            need to search for alternate tools for free private github pages -- static.app/sites fast enough (https://lime-otter.static.domains/)
            

- **Doubts**
    - whats stopping us to use Windows instead of linux (LOL had existential crisis for a min)? — jetson mein linux hota hai

### Sept 13 - Sept 25

Midsem break

### Sept 4 - Sept 12 [10/20 = 50%]

- Metric targets for perception/slam/ppc to reach for a successfull integration @DEs @Ayush Rohilla — [P0]
    - **Perception:** accuracy, range, outlier%, latency ✅
        
        currently we’re at - range<10m (less than two pairs of cones visible), latency bad for stereo with sift, avg error ~3.38% for mono
        
        Range: <10m → 15+m
        
        Latency: 2-3sec / 100ms → 50ms (20hz)
        
        Avg error: ??
        
    - **SLAM:** mean squared error, cone count, matching ratio, error threshold, latency of output to ppc ❌
        
        currently we’re at - min range that works is~20m with custom_meas of super accuracy, at about ~2m/s max velocity — nahi to it’s not able to complete the whole lap
        
        were getting mean squared error of ~0.01 m^2, correct cone count for a lap (didn’t calculate matching ratio / error threshold yet), latency ~100hz with update from meas ~20hz 
        
        - (noisy fake_meas ke saath try….)
        - why multiple freq in IMU?
        - extra cones being identified
        - discuss with @Shreyash Gupta
        
    - **PPC:** time taken in each type of event (also our north star metric), cones hit, max vel/accln
        
        raceline: 32sec, firstlap: ? (range se input leke) ✅
        
        cones hit: 0, max vel: ?, max accel: ?
        
        accln: ~6-7 sec, skidpad: ~30sec, trackdrive: ~1min (+-20sec), fastlap: fsai mein to slow slow hi (check fsg timings)
        
        **can PPC take & use gridmap???**
        
        (mainly frequency pe hi depend karega output, given error itna hai ki it can complete event)
        
        **Tentative targets in simulations**
        
        Accln: 5sec
        
        Skidpad: 20sec
        
        Autocross: 45sec
        
        Trackdrive: 35sec
        

- SLAM - which algorithms to prioritize on? (tough question!) @Shreyash Gupta @Ayush Rohilla — [P0] ✅
    1. **EKF meas mein use fake meas FSDS… (can debug) — root cause???**
    2. fastSLAM — port to FSDS (from fssim)
    3. graphslam — what is g2o / how to implement?
    4. mrpt — localization with range bearing (if possible)

- Which simulator to continue on?
    - Carmaker (global cones position/route coordinates? & IMU sensor add?) @Mohak Vyas — [P0] ✅
    - FSDS (depthmap isn’t correct!) @Mohak Vyas @Yash Rampuria — [P1] ❌
    - FSSIM (why did we discontinue this + current state?) @Ayush Rohilla — [P1] ❌
    - Steps to create our own simulator @Mohak Vyas — [P2] ❌

- Different strategies to complete Accln
    - **Other ways to do accln?? — [P0]** ❌
    - Perc + PPC (with no slam) finish implementing @Yash Rampuria @Deep Boliya — [P1] ✅

- Jetson status… @Deep Boliya @Mohak Vyas @Ayush Rohilla — [P0] ✅
    
    send to Nvidia if broken / we can’t fix it :(
    not booting up, try reinstalling os +have  reach out to nvidia
    

- JDE KTs (knowledge transfer) @DEs @JDEs — [P0] ✅
    
    we want all JDEs to be able to contribute to the team asap!!
    
    have started giving them real tasks as well…
    

- Team wiki completion — [P1]
    - **Perception:** incorporate the feedbacks, more pages? @Yash Rampuria ❌
    - **SLAM:** complete MRPT page @Shreyash Gupta ❌
    - **PPC:** incorporate the feedbacks, add vehicle dynamics/controls/ads-dv page @Deep Boliya ✅
    - **Sys int:** incorporate the feedbacks, more pages (simulatation, bot) @Mohak Vyas @MG ❌
    - **Overview:** home, goal & vision 2024, compi 101, culture? @Ayush Rohilla ❌
    - Local to web, using github hosting @Ayush Rohilla ❌

- Sys architecture + repo structure @DEs @Ayush Rohilla — [P1] ✅

- Rulebook prep for quiz on Sat @DEs @JDEs — [P1] ✅