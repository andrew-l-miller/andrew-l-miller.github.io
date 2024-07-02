---
title: Machine learning to detect continuous gravitational waves
summary:  Convolutional neural networks to search for continuous waves from isolated neutron stars in non-Gaussian noise
tags:
  - Machine learning
date: 2024-07-01

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: 
  focal_point: Smart

links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example
---

Gravitational waves that are almost monochromatic and that last for thousands of years could be emitted by isolated neutron stars that have a tiny deformation on their surfaces. These deformations, colloquially called "mountains", are expected to be only a few millimenters tall, or even less! Such sources emit very weak gravitational-wave signals with respect to those that arise from compact binary mergers; however, since the signal lasts for much longer, we are able to build up our sensitivity by taking more and more data. We could possibly see such lumpy neutron stars in our Galaxy. 

While many methods exist to search for neutron stars coming from anywhere in the sky, they are computationally expensive, since every sky location must be searched over, at every frequency and at every rate of change of the frequency over time (the "spin-down"). Thus, we have developed a machine-learning based method using convolutional neural networks that is of comparable sensitivity but is significantly cheaper computationally. We have also modelled different sources of noise to see how robust our networks are against those sources in our recent [paper](https://arxiv.org/abs/2206.00882), which shows that specific training must be done to handle the effects of different noise sources. 

Currently, we are investigating alternative ways to train the networks, estimation of parameters with the networks, adding different noise sources, and specialiazing the networks to a kind of search where the sky position is known, e.g. the galactic center.
