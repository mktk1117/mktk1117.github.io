---
title: "Elevation Mapping for Locomotion and Navigation using GPU"
date: 2022-01-01
venue: arXiv preprint arXiv:2204.12876
citation: <b> Takahiro Miki</b>, Lorenz  Wellhausen, Gr, Ruben ia, Fabian  Jenelten, Timon  Homberger, Marco Hutter
---
<b> Takahiro Miki</b>, Lorenz  Wellhausen, Gr, Ruben ia, Fabian  Jenelten, Timon  Homberger, Marco Hutter
## Bibtex
```
@article{miki2022elevation
    , author = {Miki, Takahiro and Wellhausen, Lorenz and Grandia, Ruben and Jenelten, Fabian and Homberger, Timon and Hutter, Marco}
    , journal = {arXiv preprint arXiv:2204.12876}
    , title = {Elevation Mapping for Locomotion and Navigation using GPU}
    , year = {2022}
}
```
## Paper Link
[arXiv](https://arxiv.org/abs/2204.12876)

{% include figure image_path="images/elevation_mapping/main_repo.png" alt="Elevation Mapping for Locomotion and Navigation using GPU" caption="" %}

## Abstract
Perceiving the surrounding environment is crucial for autonomous mobile robots. An elevation map provides a memory-efficient and simple yet powerful geometric representation for ground robots. The robots can use this information for navigation in an unknown environment or perceptive locomotion control over rough terrain. Depending on the application, various post processing steps may be incorporated, such as smoothing, inpainting or plane segmentation. In this work, we present an elevation mapping pipeline leveraging GPU for fast and efficient processing with additional features both for navigation and locomotion. We demonstrated our mapping framework through extensive hardware experiments. Our mapping software was successfully deployed for underground exploration during DARPA Subterranean Challenge and for various experiments of quadrupedal locomotion.

## Code
[Github](https://github.com/leggedrobotics/elevation_mapping_cupy)
