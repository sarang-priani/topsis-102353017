# Topsis-Sarang-102353017

This package implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method as a Python command-line tool. It is developed as part of an academic assignment.

## Installation

pip install Topsis-Sarang-102353017

## Usage

topsis <input_file> <weights> <impacts> <output_file>

## Example

topsis data.csv "1,1,1,1,1" "+,+,+,-,-" result.csv

## Input File Requirements

- Input file must be in CSV format
- The first column should contain alternative names
- Remaining columns must contain numeric values
- Minimum three columns are required

## Output

The output CSV file contains the TOPSIS score and rank for each alternative.

## Dependencies

pandas  
numpy  

## Author

Sarang Priani  
Roll Number: 102353017  

## PyPI Link

https://pypi.org/project/Topsis-Sarang-102353017/

## License

This project is created for academic purposes.

