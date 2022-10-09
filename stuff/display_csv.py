import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

file_path = '/home/sayantan/Codes/Python/ML/Deep_Learning/ECG/12_Lead_Classification/shit.csv'
with open(file_path) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

rows = np.array(rows)
rows = rows.astype(float)
print(rows)
plt.figure()
plt.plot(rows)
plt.xlabel('leads')
plt.ylabel('readings per lead')
plt.show()

# single_lead = []
# for i in range(0, len(rows[1])):
#     sum_cols = 0
#     for j in range(0, len(rows)):
#         sum_cols = sum_cols + rows[j][i]
#     single_lead.append(sum_cols/1000)
#
# single_lead = np.array(single_lead)
# single_lead = single_lead.astype(float)
# print(single_lead)
# plt.figure()
# plt.plot(single_lead)
# plt.show()
