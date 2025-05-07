---
title: "EagleMine: Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection"
date: 2021-02-01
tags:
  - Graph
links: 
 - name: git repository
   url: "https://github.com/BGT-M/spartan2-tutorials/blob/master/EagleMine.ipynb"
---

EagleMine is a novel tree-based mining approach to recognize and summarize the micro-clusters in the histogram.

<!--more-->

Given a histogram for millions of points, what patterns exist in the distributions of point characteristics, and how can we detect them and separate anomalies in a way similar to human vision? Hence, we propose a vision guided algorithm, EagleMine, to recognize and summarize point groups in the feature spaces. EagleMine utilizes a water-level tree to capture group structures according to vision-based intuition at multiple resolutions, and adopts statistical hypothesis tests to determine the optimal groups along the tree. Moreover,EagleMine can identify anomalous micro-clusters (i.e., micro-size groups), which exhibit very similar behavior but deviate away from the majority.

Inspired by the mechanism of human vision and cognitive system,

- EagleMine detects and summarizes micro-clusters (dense blocks) in the histogram with a hierarchical tree structure (WaterLevelTree alg.),and reports the suspiciousness score of each micro-cluster based on the deviation from the normal (TreeExplore alg.).
- For the large graph, the histogram can be constructed with correlated features of graph nodes, and the micro-clusters correspond to node groups, some of them deviating from the majority and contain anomaly / suspicious objects with high probability.
- Correlated features of graph nodes can be: (in / out) Degree, # Triangle, PageRank, Hubness / Authority, Coreness, etc.
