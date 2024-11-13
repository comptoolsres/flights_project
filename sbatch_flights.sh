#!/bin/bash

#SBATCH --job-name=flights
#SBATCH --output=flights.out
#SBATCH --error=flights.err
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=magitz@ufl.edu

# Print the current working directory, hostname, and date
pwd; hostname; date

# Load the python module
module load python

# Run the python script
python flights.py --input '/blue/bsc4452/share/Class_Files/data/flights.1K.csv'


# python flights.py --input '/blue/bsc4452/share/Class_Files/data/combined_flight_data_2019-2023_selected_cols.csv'
# python flights.py --input '/blue/bsc4452/share/Class_Files/data/combined_flight_data_2004-2023_selected_cols.csv'

# Print the date again
date