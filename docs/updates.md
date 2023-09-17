# Weekly priorities

### Sept 26 - Oct 1

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