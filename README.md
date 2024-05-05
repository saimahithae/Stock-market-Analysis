# Stock Market Forecasting

---
## Abstract
This project aims to forecast stock market prices using the following models:
1. **Random Walk Simulation**  
2. **Markov Process & Hidden Markov Model (HMM)**  
3. **Optimal Portfolios & Efficient Frontier**  

## Table of Contents
1. [Introduction](#introduction)
2. [Methodologies and Results](#methodologies-and-results)
    - [Random Walk Simulation](#random-walk-simulation)
    - [Markov Process](#markov-process)
    - [Hidden Markov Model (HMM)](#hidden-markov-model-hmm)
    - [Optimal Portfolios & Efficient Frontier](#optimal-portfolios-and-efficient-frontier)
3. [Conclusion](#conclusion)
4. [References](#references)

---

## Introduction
The stock market is inherently volatile. We employ various statistical and machine learning models to analyze and forecast future stock prices, allowing investors to make more informed decisions.

## Methodologies and Results

### Random Walk Simulation
- Predicts future prices based on Geometric Brownian Motion.
- Simulated 1000 paths for Tech Mahindra and found two paths closely matching the actual trend.

### Markov Process
- Probabilistic approach predicting future states based on current stock prices.
- State probabilities calculated using a transition probability matrix.

### Hidden Markov Model (HMM)
- Extends Markov Process with hidden states.
- Applied HMM to Axis Bank data to predict market trends.

### Optimal Portfolios & Efficient Frontier
- Identifies optimal combinations of assets.
- Efficient Frontier graphically represents risk-return trade-off.

![Efficient Frontier](efficient-frontier-graph.png)

## Conclusion
Despite market randomness, techniques like Random Walk and HMM can forecast future prices. The Efficient Frontier helps visualize optimal portfolios.

## References
1. [Random Walk](https://blog.quantinsti.com/random-walk/)
2. Zhang D. & Zhang X. (2009). Study on forecasting the stock market trend based on stochastic analysis method.
3. Sarsour Wajeeh & Rijal Shamsul (2020). Forecasting stock prices in the Malaysian Construction Sector: A Markov Chain Approach.
4. Zhang Yingjian (2021). Prediction of financial time series with Hidden Markov Models.
5. Kavitha G. & Annamalai Udhayakumar (2013). Stock Market Trend Analysis Using Hidden Markov Models.
6. [Yahoo Finance](https://in.finance.yahoo.com/)

---

