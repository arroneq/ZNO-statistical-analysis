import matplotlib.pyplot as plt
import pandas as pd
import random

pd.set_option("display.max_rows", 60)
pd.set_option("display.min_rows", 15)

def data_cleaning(df,subject,label):
	cleaned_df = df.dropna(subset=[subject])
	cleaned_df = cleaned_df.reset_index(drop=True)

	# convert strings to floats in order to use .mean() later
	cleaned_df["UkrBall100"] = cleaned_df["UkrBall100"].astype("float") # UKR should be clean anyway 
	cleaned_df[subject] = cleaned_df[subject].astype("float")

	# select rows without "0.0" values:
	cleaned_df = cleaned_df.loc[(cleaned_df[subject] != 0.0) & (cleaned_df["UkrBall100"] != 0.0)]
	cleaned_df.reset_index(drop=True, inplace=True)

	print("\nCleaned " + label + " dataframe:\n\n", cleaned_df[["Birth", "SEXTYPENAME", "UkrBall100", "mathBall100", "engBall100"]], sep="")

	return cleaned_df

def random_sampling(section,label,subject,cleaned_df,sex,n):
    sex_label = []
    if (sex == "male"): 
        sex_label = ["Male", "чоловіча"]
    else: 
        sex_label = ["Female", "жіноча"]

    sex_selected_df = cleaned_df[cleaned_df["SEXTYPENAME"] == sex_label[1]]
    sex_selected_df.reset_index(drop=True, inplace=True)
    print("\n" + sex_label[0] + " " + label + " selected dataframe:\n\n", sex_selected_df[["Birth", "SEXTYPENAME", "UkrBall100", "mathBall100", "engBall100"]], sep="")
    
    # in the sections below we are only interested in a single randomized sample formation
    if (section == "Initial data histogram" or section == "Chi-squared homogeneity hypothesis"):
        N = 1

    if (section == "Confidence interval"):
        # choose a smaller population size
        if (label == "UKR" or label == "ENG"):
            if (sex == "male"): population_size = sex_selected_df.last_valid_index()
            if (sex == "female"): population_size = cleaned_df.last_valid_index() - sex_selected_df.last_valid_index() 
        if (label == "MATH"):
            if (sex == "male"): population_size = cleaned_df.last_valid_index() - sex_selected_df.last_valid_index()
            if (sex == "female"): population_size = sex_selected_df.last_valid_index() 
        
        N = population_size//n

    index = [i for i in range(0,sex_selected_df.last_valid_index()+1)]

    means = []
    set_of_means = {}
    set_of_means.update({subject: means}) 

    for i in range(N):
        elements = []
        random_elements = {}
        random_elements.update({subject: elements})

        for j in range(n):
            random_index = random.choice(index)
            elements.append(sex_selected_df.loc[random_index, subject])
            index.remove(random_index)

        random_selected_df = pd.DataFrame(random_elements)

        means.append(random_selected_df[subject].mean())

    set_of_means = pd.DataFrame(set_of_means)

    if (section == "Initial data histogram" or section == "Chi-squared homogeneity hypothesis"):
        return random_selected_df

    # deviation
    S = 0
    for i in set_of_means.index:
        S = S + pow(set_of_means.loc[i, subject] - set_of_means[subject].mean(), 2)
    S = S/(N-1)
        
    return set_of_means, S

def paint_subplot(subnumber,data,title,boxes,colour):
    plt.subplot(1,2,subnumber)
    plt.grid(axis='y')
    plt.title(title)

    return plt.hist(data, bins=boxes, rwidth=0.9, color=colour)

def initial_data_histogram(section,label,subject,cleaned_df):
    while True:
        sample_size = input("Type in a sample size, please: ")
        try:
            n = int(sample_size)
            break
        except ValueError:
            print("Only integers are allowed!\n") 

    men_selected_df = random_sampling(section,label,subject,cleaned_df,"male",n)
    women_selected_df = random_sampling(section,label,subject,cleaned_df,"female",n)

    sex_selected_df = [men_selected_df, women_selected_df]

    if (label == "UKR"): plt.figure(figsize=(16.4, 5)).suptitle("Українська мова")
    if (label == "MATH"): plt.figure(figsize=(16.4, 5)).suptitle("Математика")
    if (label == "ENG"): plt.figure(figsize=(16.4, 5)).suptitle("Англійська мова")

    paint_subplot(1,sex_selected_df[0][subject],"Чоловіки",20,"blue")
    paint_subplot(2,sex_selected_df[1][subject],"Жінки",20,"gray")

    plt.show()

def homogeneity_hypothesis(section,label,subject,cleaned_df):
    while True:
        men_sample_size, women_sample_size = input("Type in a men sample size, please: "), input("Type in a women sample size, please: ")
        try:
            n = int(men_sample_size)
            m = int(women_sample_size)
            break
        except ValueError:
            print("Only integers are allowed!\n")

    high_marks = [[], []]    # "sex_id = 0" for men, "sex_id = 1" for women
    medium_marks = [[], []]
    low_marks = [[], []]

    high_threshold_value = 178      # 65% of subjects are available
    low_threshold_value = 144       # 29,5% of subjects are available

    men_selected_df = random_sampling(section,label,subject,cleaned_df,"male",n)
    women_selected_df = random_sampling(section,label,subject,cleaned_df,"female",m)

    sex_selected_df = [men_selected_df, women_selected_df]

    for sex_id in [0,1]:
        for i in sex_selected_df[sex_id].index:
            if (sex_selected_df[sex_id].loc[i, subject] > high_threshold_value):
                high_marks[sex_id].append(sex_selected_df[sex_id].loc[i, subject])
            elif (sex_selected_df[sex_id].loc[i, subject] < low_threshold_value):
                low_marks[sex_id].append(sex_selected_df[sex_id].loc[i, subject])
            else: 
                medium_marks[sex_id].append(sex_selected_df[sex_id].loc[i, subject])

    for sex_id, sex in [0,"men"], [1,"women"]:
        print("\nThe number of " + sex + " with high marks:", len(high_marks[sex_id]))
        print("The number of " + sex + " with medium marks:", len(medium_marks[sex_id]))
        print("The number of " + sex + " with low marks:", len(low_marks[sex_id]))
        print("nThe number of " + sex + " :", len(high_marks[sex_id]) + len(medium_marks[sex_id]) + len(low_marks[sex_id]))

    print("\nThe number of students in a sample:", sex_selected_df[0][subject].count() + sex_selected_df[1][subject].count())

def confidence_interval(section,label,subject,cleaned_df):
    while True:
        sample_size = input("Type in a sample size, please: ")
        try:
            n = int(sample_size)
            break
        except ValueError:
            print("Only integers are allowed!\n")

    men_means, Sx = random_sampling(section,label,subject,cleaned_df,"male",n)
    women_means, Sy = random_sampling(section,label,subject,cleaned_df,"female",n)

    sex_means = [men_means, women_means]

    print("\nMale means " + label + " selected dataframe:\n\n", sex_means[0][subject], sep="")
    print("\nFemale means " + label + " selected dataframe:\n\n", sex_means[1][subject], sep="")

    X_mean = sex_means[0][subject].mean()
    Y_mean = sex_means[1][subject].mean()

    print("\nSx:", Sx, "Sy:", Sy)
    print("Y.mean() - X.mean():", Y_mean - X_mean)

    plt.figure(figsize=(16.4, 5)).suptitle("Розподіли середніх значень")

    paint_subplot(1,sex_means[0][subject],"Чоловічі середні",12,"blue")
    paint_subplot(2,sex_means[1][subject],"Жіночі середні",12,"gray")

    plt.show()