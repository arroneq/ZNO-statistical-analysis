import pandas as pd

def loading_data():
    print("Please, wait a minute, the dataframe is loading")

    try:
        df = pd.DataFrame(pd.read_csv("opendatazno2019.csv", dtype="unicode"))
    except FileNotFoundError:
        exit("""\nNo data is available. Load the data!
    Hint: follow instructions in a README.md file""")
    else:
        print("\nWhole initial dataframe:\n\n", df[["Birth", "SEXTYPENAME", "UkrBall100", "mathBall100", "engBall100"]], sep="")
        return df

def choosing_subject():
    print("""\nChoose a subject:
    1. Ukrainian 
    2. Mathematics
    3. English """)

    subject_type = input("\nPlease, type in a subject number: ")

    while(subject_type not in ["1","2","3"]):
        subject_type = input("Type in a correct number: ")

    if (subject_type == "1"): subject, label = "UkrBall100", "UKR"
    if (subject_type == "2"): subject, label = "mathBall100", "MATH"
    if (subject_type == "3"): subject, label = "engBall100", "ENG"

    return subject, label

def choosing_section():
    print("""\nChoose a section:
    1. Initial data histogram
    2. Chi-squared homogeneity hypothesis
    3. Confidence interval 
    4. Exit """)

    section_type = input("\nPlease, type in a section number ")

    while(section_type not in ["1","2","3","4"]):
        section_type = input("Type in a correct number: ")

    if (section_type == "1"): section = "Initial data histogram"
    if (section_type == "2"): section = "Chi-squared homogeneity hypothesis"
    if (section_type == "3"): section = "Confidence interval"
    if (section_type == "4"): exit()
    
    return section