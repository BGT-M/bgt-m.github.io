---
title: "spartan2: a developing open-sourced graph and time series mining package based on sparse tensor/matrix and sequential analysis."
date: 2020-11-06
tags:
  - Graph
links: 
 - name: git repository
   url: "https://github.com/BGT-M/spartan2"
---

spartan2 is a collection of data mining algorithms on big graphs and time series, providing *three* basic tasks: *anomaly detection*, *forecast*, and *summarization*.

<!--more-->

Graphs and time series are fundamental representations of many key applications in a wide range of

- online user behaviors, e.g. *following in social media*, *shopping*, and *downloading Apps*,
- finance, e.g. *stock tradings, and bank transfers*,
- sensor networks, e.g. *sensor readings, and smart power grid*, and
- health, e.g. *electrocardiogram, photoplethysmogram, and respiratory inductance plethysmography*.

In practice, we find that thinking graphs and time series as matrices or tensors can enable us to find *efficient (near linear)*, *interpretable*, yet *accurate* solutions in many applications. Therefore, our goal is developping a collectioin of algorithms on graphs and time series based on tensors (matrix is a 2-mode tensor).

In real world, those tensors are *sparse*, and we are required to make use of the sparsity to develop efficient algorithms. That is why we name the package as spartan: sparse tensor analytics.

The package named spartan can be imported and run independently as a *usual python package*. Everything in package spartan is viewed as a tensor (sparse).
