---
title: "EigenPulse: Detecting surges in large streaming graphs with row augmentation"
date: 2019-04-14
tags:
  - Graph
links: 
 - name: code
   url: "https://github.com/BGT-M/spartan2-tutorials/blob/master/EigenPulse.ipynb"
---

EigenPulse is a streaming algorithm to detect surges of sliding windows in real time.

<!--more-->

How can we spot dense blocks in a large streaming graph efficiently? Anomalies such as fraudulent attacks, spamming, and DDoS attacks, can create dense blocks in a short time window, emerging a surge of density in a streaming graph. However, most existing methods detect dense blocks in a static graph or a snapshot of dynamic graphs, which need to inefficiently rerun the algorithms for a streaming graph. Moreover, some works on streaming graphs are either consuming much time on updating algorithm for every incoming edge, or spotting the whole snapshot of a graph instead of the attacking sub-block. Therefore, we propose a row-augmented matrix with sliding window to model a streaming graph, and design the AugSVD algorithm for computation- and memory-efficient singular decomposition. EigenP ulse is then proposed to spot the density surges in streaming graphs based on the singular spectrum. We theoretically analyze the robustness of our method. Experiments on real datasets with injections show our perfor- mance and efficiency compared with the state-of-the-art baseline.
