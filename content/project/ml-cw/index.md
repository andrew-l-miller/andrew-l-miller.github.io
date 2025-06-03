---
title: Machine learning to detect continuous gravitational waves
summary:  Convolutional neural networks to search for continuous waves from isolated neutron stars in non-Gaussian noise
tags:
  - Machine learning
# date: '2016-04-27T00:00:00Z'

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

We can use convolutional neural networks (CNNs) to find continuous gravitational waves, faint signals from spinning, nonaxisymmetric neutron stars. These signals can be hidden by noise or disturbances in the detectors. We have shown in [our recent paper](https://arxiv.org/abs/2206.00882) how a CNN can distinguish between real signals, Gaussian noise, and “line noise” (monochromatic disturbances in the data). We have shown that CNNs analyze the data more efficiently than traditional methods, but, like other methods, suffer a sensitivity loss when line noise is present.
