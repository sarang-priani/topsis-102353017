import sys
import pandas as pd
import numpy as np
import os

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <inputFile> <weights> <impacts> <outputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2].split(',')
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    if not os.path.exists(input_file):
        print("Error: Input file not found")
        sys.exit(1)

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit(1)

    try:
        matrix = data.iloc[:, 1:].astype(float).values
    except:
        print("Error: From 2nd column onward, all values must be numeric")
        sys.exit(1)

    if len(weights) != matrix.shape[1] or len(impacts) != matrix.shape[1]:
        print("Error: Number of weights, impacts and criteria must be same")
        sys.exit(1)

    weights = np.array(weights, dtype=float)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be '+' or '-' only")
            sys.exit(1)

    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for j in range(weighted.shape[1]):
        if impacts[j] == '+':
            ideal_best.append(weighted[:, j].max())
            ideal_worst.append(weighted[:, j].min())
        else:
            ideal_best.append(weighted[:, j].min())
            ideal_worst.append(weighted[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    scores = d_worst / (d_best + d_worst)

    data["Topsis Score"] = scores
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
    print("TOPSIS completed successfully")

if __name__ == "__main__":
    main()

