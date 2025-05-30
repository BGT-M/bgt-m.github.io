---
title: "HoloScope: Topology-and-Spike Aware Fraud Detection"
date: 2017-11-07
tags:
  - graph
links: 
 - name: git repository
   url: "https://github.com/shenghua-liu/HoloScope"
---

HoloScope is developped for fraud detection based on graphs, which makes holistic use of several signals, namely connectivity (i.e., topology), temporal bursts and drops, and rating deviation in a systematic way.

<!--more-->

As online fraudsters invest more resources, including purchasing large pools of fake user accounts and dedicated IPs, fraudulent attacks become less obvious and their detection becomes increasingly challenging. Existing approaches such as average degree maximization suffer from the bias of including more nodes than necessary, resulting in lower accuracy and increased need for manual verification. Hence, we propose HoloScope, which uses information from graph topology and temporal spikes to more accurately detect groups of fraudulent users. In terms of graph topology, we introduce *contrast suspiciousness*, a dynamic weighting approach, which allows us to more accurately detect fraudulent blocks, particularly low-density blocks. In terms of temporal spikes, HoloScope takes into account the sudden bursts and drops of fraudsters' attacking patterns. In addition, we provide theoretical bounds for how much this increases the time cost needed for fraudsters to conduct adversarial attacks. Additionally, from the perspective of ratings, HoloScope incorporates the deviation of rating scores in order to catch fraudsters more accurately. Moreover, HoloScope has a concise framework and sub-quadratic time complexity, making the algorithm reproducible and scalable. Extensive experiments showed that HoloScope achieved significant accuracy improvements on synthetic and real data, compared with state-of-the-art fraud detection methods.
