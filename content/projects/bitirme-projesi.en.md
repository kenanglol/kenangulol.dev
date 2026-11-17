---
title: "A hybrid deep learning model for stock forecasting"
slug: "stock-forecasting"
description: "My graduation thesis at Ege University: forecasting stock and index prices by combining ARIMA, a neural network and technical indicators. Funded by TÜBİTAK 2209-A."
status: "harbour"
years: "2021"
role: "B.Sc. thesis, Ege University"
stack: ["Python", "ARIMA", "Neural network (MLP)", "scikit-learn"]
weight: 3
---

My B.Sc. thesis in Computer Engineering at Ege University, completed in July 2021 under the supervision of Dr. Özgür Gümüş. The budget for data and computing tools came from TÜBİTAK's 2209-A research programme for undergraduate students.

## The problem

Stock prices are a time series, so both statistical models such as ARIMA and neural networks are common in price forecasting. The literature also has hybrid models that combine the two: they split the series into a linear and a non-linear part and give each part to the model that suits it. I built on that structure and studied how forecasting accuracy changes when the indicators used in technical analysis are added as well.

## The model

1. The price series is made stationary, by differencing or taking logarithms, until it passes the Dickey-Fuller test.
2. A moving average splits the series in two: the moving average itself is the linear part, and its difference from the raw data is the non-linear part.
3. ARIMA forecasts the linear part.
4. A neural network takes the ARIMA forecast, the non-linear part, the raw values of the previous days and the selected technical indicators together. Its output is the final price forecast.

I derived 42 technical indicators from the daily open, close, high, low and volume. Feeding all of them in made results worse, even worse than ARIMA alone. So I used scikit-learn's SelectKBest to pick the indicators most correlated with the closing price. The same indicators came out on top in four of the five data sets: VWAP, SMA12, EMA12, EMA26 and Ichimoku. The network's parameters were tuned with grid search.

## Data

Three stocks and two indices, with daily data:

- **FROTO** (Ford Otosan), 2016 – 2021
- **S&P 500**, 1997 – 2019
- **TUPRS** (Tüpraş), 2008 – 2021
- **XBANK** (BIST Banks index), 2008 – 2021
- **YKBNK** (Yapı Kredi), 2006 – 2019

FROTO, TUPRS and the S&P 500 rise steadily over the long run, while XBANK and YKBNK go up and down over the years. That difference mattered for checking whether the model also works on series with a different character.

## Results

I compared the proposed model with ARIMA alone, a neural network alone, Zhang's hybrid method and Büyükşahin's hybrid method. I also ran the other models on the data from their own papers and checked that the results matched the published ones. The table shows MAPE; lower is better.

| Data set | ARIMA | ANN | Zhang | Büyükşahin | Proposed |
|---|---:|---:|---:|---:|---:|
| FROTO | 2.22 | 2.41 | 1.72 | 0.71 | **0.55** |
| S&P 500 | 0.59 | 0.76 | 0.59 | 0.58 | **0.34** |
| TUPRS | 1.45 | 1.66 | 1.38 | 1.65 | **0.27** |
| XBANK | 1.69 | 1.90 | 1.67 | 1.82 | **0.48** |
| YKBNK | 1.38 | 1.62 | 1.56 | 1.62 | **0.20** |

The proposed model had the lowest error on all five data sets, on all three measures: MAE, MSE and MAPE. The gap was widest on TUPRS and YKBNK. Among the other models, the order was Zhang's method, ARIMA, Büyükşahin's method, and the neural network alone.

## Limits

- Most of the gain comes from the technical indicators. That ties the model to stock and index data; it would not have the same advantage on other time series.
- The indicators need more than the closing price: they also need the open, high, low and volume. So the model suits short-term forecasting and cannot make long-term forecasts.

As a next step, I expected that replacing the multilayer perceptron in the hybrid with recurrent networks (RNN, LSTM) would improve accuracy further.
