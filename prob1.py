import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy

filename = "Problem Set 1 Data.xlsx"

with open(filename, "rb") as f:
	p1_df = pd.read_excel(f, sheet_name="Problem 1")
	p2_df = pd.read_excel(f, sheet_name="Problem 2")
	p3_df = pd.read_excel(f, sheet_name="Problem 3")
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
#print(f"Mean: {x_bar}\nMedian: {x_median}\nMode: {x_mode}")

std_dev = np.std(hours_slept)
#print(std_dev)

min_val = np.min(hours_slept)
#print(min_val)
min_val_index = np.argmin(hours_slept)
#print(min_val_index)

"""
Problem 2
"""

p2_dict = {"success": 0, "failure": 0}

for res in p2_df["Treatment Outcome"]:
	if res == 0:
		p2_dict["failure"] += 1
	else:
		p2_dict["success"] += 1

success_rate = p2_dict["success"] / (p2_dict["success"] + p2_dict["failure"])

#print(f"Success rate: {success_rate}")

fig, ax = plt.subplots()
ax.pie([p2_dict["success"], p2_dict["failure"]], labels=["Success", "Failure"], autopct='%1.1f%%')
plt.show()
