---
title: Machine Learning Tutorial on Classifying Gravitational-Wave Signals
subtitle: Learn about building convolutional neural networks to correctly classify spectrograms as containing a gravitational-wave signal or just noise.

# Summary for listings and search engines
summary: Classify spectrograms as containing a transient continuous wave signal from a rapidly spinning down neutron star or as having only noise.

# Link this post with a project
projects: []

# Date published
date: '2025-06-10T00:00:00Z'

# Date updated
lastmod: '2025-06-10T00:00:00Z'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Spectrogram with injection'
  focal_point: ''
  placement: 2
  preview_only: false

authors:
  - admin

# tags:
#  - Academic

# categories:
#  - Demo
---


## Overview

1. Deformed, newborn, isolated neutron stars could spin down rapidly due to the loss of energy via gravitational waves. Because mountains on newborn neutron stars are expected to be large, the spin-down is also large, of O(0.1) Hz/s. However, the rapid rate of change of the frequency implies that the mountains quickly decrease in size, meaning that the signal duration is on the order of hours-days; hence, these signals are called transient continuous gravitational waves: longer than black hole mergers, but shorter than canonical continuous waves from older, slowly spinning down neutron stars.
2. In this tutorial, we show how convolutional neural networks can be applied to distinguish between time-frequency spectrograms containing a tCW signal, and those containing only noise. Machine learning represents a great avenue of approach for such signals, since much of the physics that governs neutron-star spindown in the early stages of its life are uncertain and equation-of-state dependent.
3. You can access the tutorial on [google collab](https://colab.research.google.com/drive/1NpmDG3ZUyyq9PiiLsRyjginqRNbQmtQ3?usp=sharing).
