# TOPSIS Assignment – Sarang Priani (Roll No: 102353017)

This repository contains the complete implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method developed as part of an academic assignment.

The project is divided into three parts:
1. Command Line Interface (CLI)
2. Python Package uploaded to PyPI
3. Web-based TOPSIS application

---

## What is TOPSIS?

TOPSIS is a Multi-Criteria Decision Making (MCDM) method used to rank alternatives based on their distance from the ideal best and ideal worst solutions. The alternative closest to the ideal best and farthest from the ideal worst is ranked highest.

---

## Repository Structure

topsis-102353017/
│
├── Part1_CLI/        # Command-line TOPSIS implementation
├── part2package/     # Python package uploaded to PyPI
├── topsis-web/       # Web-based TOPSIS application
└── README.md

---

## Part I – Command Line Interface (CLI)

Folder: `Part1_CLI`

This part implements TOPSIS as a Python command-line program.

### Usage

python3 topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFile>

### Example

python3 topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv

### Features and Validations
- Checks correct number of command-line arguments
- Handles file not found exception
- Input file must contain at least three columns
- From second to last column must contain numeric values only
- Number of weights, impacts, and criteria must be equal
- Impacts must be either + or -
- Weights and impacts must be comma-separated
- Generates output CSV with Topsis Score and Rank

---

## Part II – Python Package (PyPI)

Folder: `part2package`

The CLI implementation is packaged and published on PyPI.

### PyPI Package Link

https://pypi.org/project/Topsis-Sarang-102353017/

### Installation

pip3 install Topsis-Sarang-102353017

### Usage After Installation

topsis data.csv "1,1,1,1,1" "+,+,+,-,-" result_from_package.csv

### Package Details
- Package Name: Topsis-Sarang-102353017
- Version: 0.0.4
- Author: Sarang Priani
- Dependencies: numpy, pandas
- Tested by installing from PyPI and running via terminal

---

## Part III – Web Application

Folder: `topsis-web`

A Flask-based web application to perform TOPSIS using a browser interface.

### Features
- Upload CSV file
- Enter weights and impacts
- Enter email ID
- Generate TOPSIS result
- Display success or error messages
- Email functionality implemented (subject to network restrictions)

### How to Run

python3 app.py

Open browser and visit:
http://127.0.0.1:5000

---

## Input and Output Format

Input CSV:
- First column: Alternative names
- Remaining columns: Numeric criteria values

Output CSV:
- Original data
- Added columns:
  - Topsis Score
  - Rank

---

## Author

Sarang Priani  
Roll Number: 102353017  

---

## Conclusion

This repository demonstrates a complete end-to-end implementation of the TOPSIS method including CLI usage, Python package distribution via PyPI, and a web-based application interface.
