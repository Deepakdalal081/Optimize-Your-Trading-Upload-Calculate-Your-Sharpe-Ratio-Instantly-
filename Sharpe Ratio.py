# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:52:04 2025

@author: Deepak Dalal

"""

import pandas as pd
import numpy as np
import yfinance as yf

# File path to the Excel data
file_path = "C:\\Users\\sdhan\\Desktop\\EPAT 62\\Project\\Sharpe Ratio.xlsx"

# Read Excel file into DataFrame
df = pd.read_excel(file_path)
Sharpe_ratio = pd.DataFrame(df)

# Calculate the percentage return for each trade
Sharpe_ratio["Return"] = ((Sharpe_ratio["Sell Value"] - Sharpe_ratio["Buy Value"]) / Sharpe_ratio["Buy Value"]) * 100

# Compute standard deviation (std) of returns
std = np.std(Sharpe_ratio["Return"])

# Compute mean return
mean_of_return = np.mean(Sharpe_ratio["Return"])

# Count total number of trades
no_of_trades = len(Sharpe_ratio)

# Calculate mean difference squared for variance calculation
Sharpe_ratio["Mean"] = Sharpe_ratio["Return"].mean()
Sharpe_ratio["Mean_Diff"] = (Sharpe_ratio["Return"] - Sharpe_ratio["Mean"])**2

# Compute standard deviation (std) of returns by another way
mean_difference_sum = np.sqrt(Sharpe_ratio["Mean_Diff"].sum() / (no_of_trades - 1))

# Compute Sharpe Ratio
Sharpe_ratio_trades = mean_of_return / mean_difference_sum

# Print Sharpe Ratio results

print("----------------------------")
print(f"Sharpe Ratio of trades: {Sharpe_ratio_trades:.4f}")

# Interpretation of Sharpe Ratio
if Sharpe_ratio_trades > 2:
    print("Excellent risk-adjusted return: Your strategy is performing very well with high returns compared to the risk taken.")
elif 1 < Sharpe_ratio_trades <= 2:
    print("Good but not exceptional performance: The strategy is profitable but involves moderate risk. Consider optimizing it further.")
else:
    print("High risk compared to return: The strategy's risk is too high relative to its returns. Adjustments are needed to improve stability.")

# Sortino Ratio Calculation
# Filtering negative returns for downside risk calculation
Sharpe_ratio["Negative Return"] = Sharpe_ratio["Return"][Sharpe_ratio["Return"] < 0]

# Compute downside deviation (std of negative returns)
std_of_negative_return = Sharpe_ratio["Negative Return"].std()

# Compute Sortino Ratio
Sortino_ratio = mean_of_return / std_of_negative_return

# Print Sortino Ratio results
print("--------------------------------------")
print(f"Sortino Ratio for this strategy: {Sortino_ratio:.4f}")

# Interpretation of Sortino Ratio
if Sortino_ratio > 2.5:
    print("Exceptional risk-adjusted returns: Your strategy effectively minimizes downside risk while maintaining strong returns.")
elif 1 < Sortino_ratio <= 2.5:
    print("Decent but has some downside risk: The strategy is performing well, but there is still some exposure to losses.")
else:
    print("High downside risk: Your strategy carries significant risk of losses. Consider making adjustments to reduce exposure to negative returns.")
