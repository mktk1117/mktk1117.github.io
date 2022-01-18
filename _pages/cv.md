---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S. in Aeronautics and Astronautics, The University of Tokyo, 2011-2015
  * Graduated with a major GPA 3.78/4.0, overall GPA 3.59/4.0
  * Concentration in Astronautics, Control Engineering, and Artificial Intelligence
  * Thesis topic: Self Localization with Active Attachment of AR Markers by Autonomous UAV.
* M.S. in Aeronautics and Astronautics, The University of Tokyo, 2015-2018
  * Topic: UAV/UGV Autonomous Cooperation: UAV Assists UGV to Climb a Cliff by Attaching a Tether.
  * Making a rover that can climb the wall by winding a tether attached by a drone.
  * GPA 3.92/4.0
* Exchange in Department of Mechanical and Process Engineering, ETH Zurich, 2016-2017
  * Project: Mapping and Trajectory Planning for Legged Robots at Robotics Systems Lab (RSL)
  * Multi-agent Time-based Decision-making for the Search and Action Problem. Project for the MBZIRC Robotics Challenge at Autonomous Systems Lab (ASL)
* Ph.D at Robotic Systems Lab, ETH Zurich, 2019-present
  * Reinforcement learning for perceptive locomotion of quadrupedal robot ANYmal
  * Team member of CERBERUS at DARPA Subterranean Challenge. Won the first prize.

Work experience
======
* 2018 - 2019: Researcher at Hitachi, Ltd. Research & Development Group
  * Researching AI for robot (Deep learning, Reinforcement Learning etc.) 
  * Aimed for robot decommissioning Fukushima nuclear power plant.

* 2017 - 2018: Internship at ispace.inc
  * Worked for Lunar exploration rover.
  * ToF camera data processing and making elevation map.
  * Made Gazebo simulator package of space exploration rover on moon surface.

* 2016 - 2018: Part-time at Hongo Aerospace, inc
  * Built a drone with custom made flight controller and Jetson TX2.
  * Autonomous flying using Visual Inertial Odometry, Model Predictive Control and Local path planning for obstacle avoidance using 3D signed distance field.
  
Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
