---
title: "BeatGAN: Anomalous Rhythm Detection using Adversarially Generated Time Series."
date: 2019-08-10
tags:
  - Graph
links: 
 - name: git repository
   url: "https://github.com/BGT-M/spartan2-tutorials/blob/master/BeatGAN.ipynb"
---

<!--more-->

Given a large-scale rhythmic time series containing mostly normal data segments (or ‘beats’), can we learn how to detect anomalous beats in an effective yet efficient way? For example, how can we detect anomalous beats from electrocardiogram (ECG) readings? Existing approaches either require excessively high amounts of labeled and balanced data for classification, or rely on less regularized reconstructions, resulting in lower accuracy in anomaly detection. Therefore, we propose BeatGAN, an unsupervised anomaly detection algorithm for time series data. BeatGAN outputs explainable results to pinpoint the anomalous time ticks of an input beat, by comparing them to adversarially generated beats. Its robustness is guaranteed by its regularization of reconstruction error using an adversarial generation approach, as well as data augmentation using time series warping. Experiments show that BeatGAN accurately and efficiently detects anomalous beats in ECG time series, and routes doctors’ attention to anomalous time ticks, achieving accuracy of nearly 0.95 AUC, and very fast inference (2.6 ms per beat). In addition, we show that BeatGAN accurately detects unusual motions from multivariate motion-capture time series data, illustrating its generality.
