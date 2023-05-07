# Where to find the results?

You may find out all the information concerning statistical analysis in a .pdf file located at ```SA-LATEX/main.pdf```.

# How to use LaTeX code?

Just few steps to follow:
1. Install $\LaTeX$ on your local machine;
2. Clone a repository using ```git clone https://github.com/Arroneq/SA-LATEX.git``` or download it as a ZIP;
3. Run ```SA-LATEX/main.tex``` file.

Congratulations! Now you can easily discover ```.tex``` code!

# How to use Python code?



## What is the project for?

The main purpose of a written code (```SA-PYTHON``` folder) is to manage the data and calculate all the necessary values, used in statistic analysis. 

## How to use the code?

Download such files: ```SA.py``` (set of calculation methods), ```UI.py``` (user interface) and ```main.py``` (business logic). Then keep going step by step through the instructions below.

### Required to install

You should have this software be installed:

- ```Python``` (3+ version) and the following libraries: 
    - ```xlrd```
    - ```csv``` 
    - ```matplotlib``` 
    - ```pandas``` 
    - ```random```

But notice, that version of ```xlrd``` library should be only 1.2.0. To do so, you may run 

```bash
pip3 install xlrd==1.2.0
```

### Loading the data

The next step is to load the data onto your local machine. First things first go to https://osvita.ua/news/data/69491/ and click a "Download" red button. After that unzip files and convert ```opendatazno2019.xlsx``` into ```opendatazno2019.csv``` via the code below:

```python
import pandas as pd
import xlrd 
import csv
    
# open workbook by sheet index, optional - sheet_by_index()
sheet = xlrd.open_workbook("opendatazno2019.xlsx").sheet_by_index(0)
    
column = csv.writer(open("opendatazno2019.csv", "w", newline=""))
    
# row by row rewrite the data into csv file
for row in range(sheet.nrows):
    column.writerow(sheet.row_values(row))
    
# convert file into a dataframe object
df = pd.DataFrame(pd.read_csv("opendatazno2019.csv", dtype="unicode"))
```

### Running the code

Keep both ```.py``` and ```.csv``` files in the same folder. Congratulations, now you are ready to run the ```main.py``` file!

# Contact information

If you have any questions or comments about this project, please feel free to contact me in any of the following ways:

- Email: [anton.tsybulnik@gmail.com](mailto:anton.tsybulnik@gmail.com)
- Telegram: [@arroneq](https://t.me/arroneq)