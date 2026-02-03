import sys
import pandas as pd
import numpy as np
import os

if len(sys.argv) != 5:
    print("Usage: python3 topsis.py <inputFile> <weights> <impacts> <outputFile>")
    sys.exit(1)

input_file = sys.argv[1]
weights = sys.argv[2].split(",")
impacts = sys.argv[3].split(",")
output_file = sys.argv[4]

if not os.path.exists(input_file):
    print("Error: Input file not found")
    sys.exit(1)

try:
    df = pd.read_csv(input_file)
except:
    print("Error: Unable to read input file")
    sys.exit(1)

if df.shape[1] < 3:
    print("Error: Input file must contain at least 3 columns")
    sys.exit(1)

data = df.iloc[:, 1:]

try:
    data = data.astype(float)
except:
    print("Error: Non-numeric values found in criteria columns")
    sys.exit(1)

if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
    print("Error: Number of weights, impacts and criteria must be same")
    sys.exit(1)

for i in impacts:
    if i not in ['+', '-']:
        print("Error: Impacts must be + or -")
        sys.exit(1)

weights = np.array(weights, dtype=float)

norm = np.sqrt((data ** 2).sum())
weighted = (data / norm) * weights

ideal_best = []
ideal_worst = []

for i in range(len(impacts)):
    if impacts[i] == '+':
        ideal_best.append(weighted.iloc[:, i].max())
        ideal_worst.append(weighted.iloc[:, i].min())
    else:
        ideal_best.append(weighted.iloc[:, i].min())
        ideal_worst.append(weighted.iloc[:, i].max())

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

score = d_worst / (d_best + d_worst)

df["Topsis Score"] = score
df["Rank"] = score.rank(ascending=False).astype(int)

df.to_csv(output_file, index=False)

print("TOPSIS calculation completed successfully")

