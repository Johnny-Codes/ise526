import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "Problem Set 1 Data.xlsx"

with open(filename, "rb") as f:
	p1_df = pd.read_excel(f, sheet_name="Problem 1")

#print(df)

"""
1) Describe in detail the distribution of the sleep times. Go beyond simply naming the shape - discuss all of its properties.
"""

hours_slept = p1_df["Hours Slept"]

data_dict = {}

for hrs in hours_slept:
	if hrs not in data_dict:
		data_dict[hrs] = 1
	else:
		data_dict[hrs] += 1

#print(data_dict)

#plt.scatter(data_dict.keys(), data_dict.values())
#plt.show()

x_bar = np.mean(hours_slept)
#x_median = np.median(hours_slept) # getting a nan with np
x_median = hours_slept.median()
x_mode = hours_slept.mode()[0]
print(f"Mean: {x_bar}\nMedian: {x_median}\nMode: {x_mode}")
