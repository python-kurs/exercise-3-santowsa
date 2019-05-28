# Exercise 3
from pathlib import Path

# import functions from utils here
import utils as uts

mainDir = Path("C:/Users/Admin/Documents/GitHub/exercise-3-santowsa/")
data_dir = mainDir / "data"
output_dir = mainDir / "solution"    

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]
carPath = data_dir / "cars.txt"

# 2. Read the text file [2P]

with open(carPath,"r") as file:
    lines = file.read().splitlines()

# 3. Count the occurences of each item in the text file [2P]

uts.countSingles(lines)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

uts.dirCreate(output_dir)


# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
import pandas as pd

output = uts.countSingles(lines,returnval=True)
outPath = output_dir / "counts.csv"
output.to_csv(outPath, header=True)