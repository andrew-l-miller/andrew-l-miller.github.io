---
title: Detector glitch classification with machine learning
summary: Identifying different kinds of glitches in LIGO data using auxiliary channels
tags:
  - machine learning
date: 2024-06-01

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

Glitches are extremely strong, random bursts of noise that affect the sensitivity of the detector. They happen very frequently, i.e. every few minutes or so, and take on many different forms. Though the origins of many are unknown, we are working on a way to classify these glitches and determine which part of the instrument they could have originated from. In our [recent work](https://arxiv.org/abs/2310.03453), we used unsupervised machine learning methods that analyze data from thousands of different channels to learn the underlying distributions of glitches, and essentially look for correlations between the different channels, and deviations from what we expect in the case of pure Gaussian noise. 
