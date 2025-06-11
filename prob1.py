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
#print(f"hours slept: {len(hours_slept)}")
low_ci = x_bar - 1.96 * (std_dev)/np.sqrt(len(hours_slept))
high_ci = x_bar + 1.96 * (std_dev)/np.sqrt(len(hours_slept))

#print(f"CI: ({low_ci}, {high_ci})")

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

#fig, ax = plt.subplots()
#ax.pie([p2_dict["success"], p2_dict["failure"]], labels=["Success", "Failure"], autopct='%1.1f%%')
#plt.show()

# z testing
k = 0
for i in p2_df["Treatment Outcome"]:
	if i == 1:
		k += 1
n = len(p2_df["Treatment Outcome"])
pvalue = .05
hypothesis = 0.9
#print(f"{k=}, {n=}, {pvalue=}")

#print(scipy.stats.binomtest(k, n, p = hypothesis, alternative="less"))

"""
Problem 3
"""

p3_ass = p3_df["Assistant"]
p3_temp = p3_df["Temperature"]
p3_fail = 0
for i in p3_df["fail"]:
	if i == 1:
		p3_fail+= 1
p3_len = len(p3_df["Run"])
#print(p3_ass)
prob_fail = p3_fail / p3_len
print(f"prob fail: {prob_fail}, prob succ = {1 - prob_fail}")
cold_total = 0
cold_success = 0
hot_total = 0
hot_success = 0

for i, r in p3_df.iterrows():
	if r["Assistant"] == "cold":
		cold_total += 1
		if r["fail"] == 0:
			cold_success += 1
	else:
		hot_total += 1
		if r["fail"] == 0:
			hot_success += 1
cold_mean = cold_success / cold_total if cold_total > 0 else 0
hot_mean = hot_success / hot_total if hot_total > 0 else 0
print(f"total cold = {cold_total}, cold_success = {cold_success}, cold_success_avg = {cold_mean}")
print(f"hot_total = {hot_total}, hot_success = {hot_success}, hot_successs_avg = {hot_mean}")


