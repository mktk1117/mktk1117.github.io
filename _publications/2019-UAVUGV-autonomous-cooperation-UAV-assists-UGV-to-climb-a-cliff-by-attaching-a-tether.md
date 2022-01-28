---
title: "UAV/UGV autonomous cooperation: UAV assists UGV to climb a cliff by attaching a tether"
date: 2019-01-01
venue: IEEE, 2019 International Conference on Robotics and Automation (ICRA)
citation: <b> Takahiro Miki</b>, Petr  Khrapchenkov, Koichi Hori
---
<b> Takahiro Miki</b>, Petr  Khrapchenkov, Koichi Hori

{% include figure image_path="images/uavugv/concept.png" alt="UAV UGV Cooperation" caption="Our proposed UAV/UGV cooperative system. The UAV provides a sensor data for mapping. In addition, the UAV attaches a tether to the structure on top of a cliff and the UGV climbs by winding it." %}

## Paper Link
[IEEE](https://ieeexplore.ieee.org/document/8794265)  
[arXiv](https://arxiv.org/abs/1903.04898) 

{% include video id="UzTT8Ckjz1M" provider="youtube" %}


## Abstract
This paper proposes a novel cooperative system for an Unmanned Aerial Vehicle (UAV) and an Unmanned Ground Vehicle (UGV) which utilizes the UAV not only as a flying sensor but also as a tether attachment device. Two robots are connected with a tether, allowing the UAV to anchor the tether to a structure located at the top of a steep terrain, impossible to reach for UGVs. Thus, enhancing the poor traversability of the UGV by not only providing a wider range of scanning and mapping from the air, but also by allowing the UGV to climb steep terrains with the winding of the tether. In addition, we present an autonomous framework for the collaborative navigation and tether attachment in an unknown environment. The UAV employs visual inertial navigation with 3D voxel mapping and obstacle avoidance planning. The UGV makes use of the voxel map and generates an elevation map to execute path planning based on a traversability analysis. Furthermore, we compared the pros and cons of possible methods for the tether anchoring from multiple points of view. To increase the probability of successful anchoring, we evaluated the anchoring strategy with an experiment. Finally, the feasibility and capability of our proposed system were demonstrated by an autonomous mission experiment in the field with an obstacle and a cliff.


## News
- Featured at IEEE Spectrum [Video Friday: This Robot Is Learning to Slice Onions The best robot videos from the world's biggest robotics conference](https://spectrum.ieee.org/video-friday-this-robot-is-learning-to-slice-onions)
- Covered by VentureBeat [Autonomous system uses quadcopters to help wheeled robots climb steep cliffs](https://venturebeat.com/2019/03/13/autonomous-system-uses-quadcopters-to-help-wheeled-robots-climb-steep-cliffs/)


## Bibtex
```
@inproceedings{miki2019uav
    , author = {Miki, Takahiro and Khrapchenkov, Petr and Hori, Koichi}
    , booktitle = {2019 International Conference on Robotics and Automation (ICRA)}
    , organization = {IEEE}
    , pages = {8041--8047}
    , title = {UAV/UGV autonomous cooperation: UAV assists UGV to climb a cliff by attaching a tether}
    , year = {2019}
}


```
