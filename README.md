# 🏃 110m Hurdle Race Time Predictor

A machine learning-powered tool that predicts your next 110m hurdle race time based on your personal race history across high school (39") and college (42") competition.

---

## Overview

This predictor takes your past 110m hurdle race times and forecasts your next performance. It accounts for the hurdle height difference between high school (39") and college (42") and uses your historical progression trend to generate a predicted time.

---

## Features

- Input race history from **high school (39") and/or college (42")**
- Normalizes times across hurdle heights for accurate comparison
- Tracks your **performance trend** over time
- Outputs a predicted time with a confidence range

---

## Tech Stack

- **Language:** Python 3.13
- **Libraries:**
  - `numpy` — numerical operations
  - `scipy` — regression and curve fitting
  - `pandas` — data handling
  - `matplotlib` — performance trend visualization
