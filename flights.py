#!/usr/bin/env python

# Import the necessary modules
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='Read and plot flight data')

# Add arguments
parser.add_argument('filename', type=str, help='the name of the CSV file to read')


# Parse the arguments
args = parser.parse_args()



# Read the data from the CSV file
data = pd.read_csv(args.filename)


